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
from bsn.common import msg_send_pkg
from bsn.common import msg_head
from bsn.common import msg

class EState(enum.Enum):
    Null = 0
    Connecting = 1
    Connected = 2
    ConnectFail = 3
    ConnectBeDisconnect = 4
    DisConnect = 5



class CTCPClient(object):
    """  
    """

    def __init__(self, loop):
        logging.info("{}".format(self))
        self._CMsgSendPkg = msg_send_pkg.CMsgSendPkg(self.send)

        self._reader = None
        self._writer = None

        self._EStateCTCPClient = EState.Null

        self._CHost = None
        self._CPort = None

        self._loop = loop

        
    async def on_recv_msg(self, cmd, byData):
        '''
        '''
        yield

    def send_pkg(self, cmd, data):
        logging.info("{} cmd={}".format(self, cmd))
        return self._CMsgSendPkg.send_pkg(cmd, data)

    def estate_tcp_client(self):
        return self._EStateCTCPClient

    def is_connected(self):
        return self.estate_tcp_client() == EState.Connected

    async def connect(self):
        '''
        '''
        logging.info("{} {} {}".format(self, self._CHost, self._CPort))
        if self.estate_tcp_client() != EState.Null:
            raise err.ErrState(self.estate_tcp_client())

        await self._connect(1)

    async def _connect(self, uRetryWaitSec):
        '''
        uRetryWaitSec
            连接失败 重试等待秒
        '''
        logging.info("{} {} {}".format(self, self._CHost, self._CPort))
        if type(self._CHost) != CHost:
            raise err.ErrHost(self._CHost)
        if type(self._CPort) != CPort:
            raise err.ErrPort(self._CPort)
        if self.estate_tcp_client() == EState.Connected:
            raise err.ErrState(self.estate_tcp_client())

        self._EStateCTCPClient = EState.Connecting
        while self.estate_tcp_client() == EState.Connecting:
            try:
                self._reader, self._writer = await asyncio.open_connection(str(self._CHost), str(self._CPort), loop=self._loop)
                break
            except ConnectionRefusedError as e:
                logging.error(e)
                await asyncio.sleep(uRetryWaitSec)  

        if self._reader is None or self._writer is None:
            logging.info("{} connect fail state={}".format(self, self.estate_tcp_client()))
            return
        logging.info("{} connect success state={}".format(self, self.estate_tcp_client()))

        self._set_keep_alive()
        self._set_nodelay(True)
        self._EStateCTCPClient = EState.Connected
        asyncio.ensure_future(self._recv_loop(), loop = self._loop)
            
    async def _recv_loop(self):
        logging.info("{}".format(self))
        try:
            oCMsgHead = msg_head.CMsgHead()
            while self.estate_tcp_client() == EState.Connected:
                byHeadData = await self._reader.readexactly(oCMsgHead.Bit)
                oCMsgHead.parse(byHeadData)
                if oCMsgHead.length > 0:
                    byBodyData = await self._reader.readexactly(oCMsgHead.length)
                    self.on_recv_msg(oCMsgHead.cmd, byBodyData)
                else:
                    self.on_recv_msg(oCMsgHead.cmd, b'')
        except asyncio.streams.IncompleteReadError as e:
            logging.error(e)
            if self.estate_tcp_client() == EState.Connected:
                logging.info("{} peer disconnect".format(self))
                self._EStateCTCPClient = EState.ConnectBeDisconnect
                asyncio.ensure_future(self._connect(1), loop = self._loop)
                return

        if self.estate_tcp_client() == EState.Connected:
            await self.disconnect('recv loop')

        self._writer = None
        self._reader = None

    async def disconnect(self, strWhy):
        logging.info("{} {}".format(self, strWhy))
        if self.estate_tcp_client() != EState.Connected:
            raise err.ErrState(self.estate_tcp_client())

        # await self.wait_all_send()
        if self._writer:
            self._writer.transport.close()
        while self.estate_tcp_client() == EState.Connected:
            await asyncio.sleep(1)

        logging.info('leave {}'.format(self))
                
    def send(self, data):
        if not self.is_connected():
            return False
        return self._writer.write(data)

    async def wait_all_send(self):
        await self._writer.drain()

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

