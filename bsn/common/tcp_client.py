#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
import socket
from bsn.common.port import CPort
from bsn.common.host import CHost
from bsn.common import err


class EState(enum.Enum):
    Null = 0
    Connected = 1



class CTCPClient(object):
    """  
    """

    def __init__(self, loop):
        logging.info("{}".format(self))
        self._reader = None
        self._writer = None

        self._EStateCTCPClient = EState.Null

        self._CHost = None
        self._CPort = None

        self._loop = loop

        self._uRetryCountMax = 30
        self._uRetryDelaySec = 1
        
        self._uPkgLengthBit = 2 # pkg length value use bit
        self._uPkgLengthMax = 10 # pkg length value max
        self._uRecvByte = 0
        self._uSendByte = 0
        self._uRecvPkg = 0
        self._uSendPkg = 0

    def estate_tcp_client(self):
        return self._EStateCTCPClient

    async def connect(self):
        '''
        '''
        logging.info("{} {} {}".format(self, self._CHost, self._CPort))
        if type(self._CHost) != CHost:
            raise err.ErrHost(self._CHost)
        if type(self._CPort) != CPort:
            raise err.ErrPort(self._CPort)
        if self._EStateCTCPClient != EState.Null:
            raise err.ErrState(self._EStateCTCPClient)

        uRetryCount = 0
        while True:
            try:
                self._reader, self._writer = await asyncio.open_connection(str(self._CHost), str(self._CPort), loop=self._loop)
                break
            except ConnectionRefusedError as e:
                logging.error(e)
                if uRetryCount >= self._uRetryCountMax:
                    return err.ErrConnectFail(e)
                uRetryCount = uRetryCount + 1
                await asyncio.sleep(self._uRetryDelaySec)

        self._set_keep_alive()
        self._set_nodelay(True)
        self._EStateCTCPClient = EState.Connected
        asyncio.ensure_future(self._recv_loop(), loop = self._loop)

    async def _recv_loop(self):
        logging.info("{}".format(self))
        try:
            while self._EStateCTCPClient == EState.Connected:
                head = await self.read_bytes(self._uPkgLengthBit)
                pkgLength = int.from_bytes(head, 'little')
                logging.info("{} head:{} pkgLength:{}".format(self, head, pkgLength))
                if pkgLength > self._uPkgLengthMax:
                    logging.info("{} head:{} pkgLength:{} self._uPkgLengthMax:{}".format(self, head, pkgLength, self._uPkgLengthMax))
                    asyncio.ensure_future(self.disconnect("pkg too big"), loop = self._loop)
                    return
                pkgData = await self.read_bytes(pkgLength)
                await self._on_recv_pkg(pkgData)
        except asyncio.streams.IncompleteReadError as e:
            logging.error(e)

    async def _on_recv_pkg(self, byData):
        logging.info("{} byData:{}".format(self, byData))
        self._uRecvPkg = self._uRecvPkg + 1
        yield

    async def disconnect(self, strWhy):
        logging.info("{} {}".format(self, strWhy))
        if self._EStateCTCPClient != EState.Connected:
            raise err.ErrState(self._EStateCTCPClient)

        await self.wait_all_send()
  
        if self._writer:
            self._writer.transport.close()
        self._writer = None
        self._reader = None

        logging.info('leave {}'.format(self))
                
    def send_pkg(self, data):
        self._uSendPkg = self._uSendPkg + 1
        length = len(data)
        byLength = length.to_bytes(2, byteorder='little')
        self.send(byLength)
        self.send(data)

    def send(self, data):
        self._uSendByte = self._uSendByte + 1
        return self._writer.write(data)

    async def wait_all_send(self):
        await self._writer.drain()

    async def read_bytes(self, num_bytes):
        data = await self._reader.readexactly(num_bytes)
        self._uRecvByte = self._uRecvByte + len(data)
        return data

    @property
    def host(self):
        return self._CHost

    @property
    def port(self):
        return self._CPort

    def _set_keep_alive(self):
        transport = self._writer.transport
        transport.pause_reading()
        raw_sock = transport.get_extra_info('socket', default=None)
        if raw_sock is None:
            raise RuntimeError("Transport does not expose socket instance")
        raw_sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        transport.resume_reading()

    def _set_nodelay(self, value):
        flag = int(bool(value))
        transport = self._writer.transport
        transport.pause_reading()
        raw_sock = transport.get_extra_info('socket', default=None)
        if raw_sock is None:
            raise RuntimeError("Transport does not expose socket instance")
        raw_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, flag)
        transport.resume_reading()

file_import_tree.file_end(__name__)

