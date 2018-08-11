#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
import socket
from bsn.common.port import CPort
from bsn.common.host import CHost
from bsn.common import err


class EState(enum.Enum):
    Null = 0
    WaitConnect = 1
    Connected = 2



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

    def start_connect(self, host, port):
        '''
        '''
        logging.info("{} {} {}".format(self, host, port))
        if type(host) != CHost:
            raise err.ErrHost(host)
        if type(port) != CPort:
            raise err.ErrPort(port)
        if self._EStateCTCPClient is not EState.Null:
            raise err.ErrState(self._EStateCTCPClient)

        self._CHost = host
        self._CPort = port
        self._EStateCTCPClient = EState.WaitConnect
        asyncio.ensure_future(self._connect(), loop=self._loop)

    def _on_connect(self):
        logging.info("{}".format(self))

    def _on_connect_fail(self):
        logging.info("{}".format(self))

    def stop_connect(self):
        logging.info("{}".format(self))
        if self._writer:
            self._writer.transport.close()
        self._writer = None
        self._reader = None

    def _on_dis_connect(self):
        logging.info("{}".format(self))

    async def _connect(self):
        """
        """
        logging.info("{} {} {}".format(self, self._CHost, self._CPort))
        
        uRetryCount = 0
        while True:
            try:
                self._reader, self._writer = await asyncio.open_connection(str(self._CHost), str(self._CPort), loop=self._loop)
                break
            except ConnectionRefusedError as e:
                logging.error(e)
                if uRetryCount >= self._uRetryCountMax:
                    self._EStateCTCPClient = EState.Null
                    self._on_connect_fail()
                    return
                uRetryCount = uRetryCount + 1
                await asyncio.sleep(self._uRetryDelaySec)
        self._set_keep_alive()
        self._set_nodelay(True)
        self._EStateCTCPClient = EState.Connected
        self._on_connect()
        asyncio.ensure_future(self._recv_loop(), loop=self._loop)
                
    def send_pkg(self, data):
        length = len(data)
        byLength = length.to_bytes(2, byteorder='little')
        self.write_bytes(byLength)
        self.write_bytes(data)

    def write_bytes(self, data):
        return self._writer.write(data)

    async def wait_all_send(self):
        await self._writer.drain()

    async def read_bytes(self, num_bytes):
        data = await self._reader.readexactly(num_bytes)
        return data

    async def _recv_loop(self):
        while self._EStateCTCPClient == EState.Connected:
            head = await self.read_bytes(self._uPkgLengthBit)
            pkgLength = int.from_bytes(head, 'little', False)
            logging.info("{} head:{} pkgLength:{}".format(self, head, pkgLength))
            if pkgLength > self._uPkgLengthMax:
                logging.info("{} head:{} pkgLength:{} self._uPkgLengthMax:{}".format(self, head, pkgLength, self._uPkgLengthMax))
                self.stop_connect()
                return
            pkgData = await self.read_bytes(pkgLength)
            logging.info("{} pkgData:{}".format(self, pkgData))
        self._on_dis_connect()
    
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



