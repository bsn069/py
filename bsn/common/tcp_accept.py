#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common.port import CPort
from bsn.common.ip import CIP
from bsn.common import err

class State(enum.Enum):
    Null = 0
    WaitListen = 1
    Listened = 2
    WaitClose = 3
    Closeing = 4
    Listening = 5


class ITCPAcceptCB(object):

    def __init__(self):
        logging.info("{}".format(self))

    def on_connect(self, stream_protocal):
        """
        accept_cb CStreamProtocol
        """
        logging.info("{}".format(self))

    def on_listen(self):
        logging.info("{}".format(self))

    def on_close(self):
        logging.info("{}".format(self))


class CStreamProtocol(asyncio.protocols.Protocol):
    """ 
    """

    def __init__(self, accept_cb):
        """
        accept_cb ITCPAcceptCB
        """
        logging.info("{}".format(self))
        self._accept_cb = accept_cb
        self._transport = None
        self._read_buff = bytearray()
        self._write_buff = bytearray()

    def connection_made(self, transport):
        logging.info("{}".format(self))
        self._transport = transport
        self._accept_cb.on_connect(self)
        self._accept_cb = None

    def connection_lost(self, exc):
        logging.info("{}".format(self))

    def data_received(self, data):
        logging.info("{} {}".format(self, data))
        self._read_buff.append(data)

    def eof_received(self):
        logging.info("{}".format(self))

    def write(self, data):
        logging.info("{} {}".format(self, data))
        self._write_buff.append(data)

    def flush(self):
        self._transport.write(self._write_buff)

    def read(self):
        return self._read_buff

    def close(self):
        return self._transport.close()
        


class CTCPAccept(object):
    """  
    """

    def __init__(self, accept_cb, loop):
        """
        accept_cb ITCPAcceptCB
        """
        logging.info("{}".format(self))
        self._loop = loop
        self._ip = None
        self._port = None
        self._state = State.Null
        self._server = None
        self._accept_cb = accept_cb

    def listen(self, ip, port):
        '''
        ip CIP
        port CPort
        '''
        logging.info("{}".format(self))
        if type(ip) != CIP:
            raise err.ErrIP(ip)
        if type(port) != CPort:
            raise err.ErrPort(port)
        if self._state is not State.Null:
            raise err.ErrState(self._state)

        self._ip = ip
        self._port = port
        self._state = State.WaitListen
        asyncio.ensure_future(self._listen(), loop=self._loop)

    def close(self):
        logging.info("{}".format(self))
        if self._state is not State.Listened:
            raise err.ErrState(self._state)

        self._state = State.WaitClose
        asyncio.ensure_future(self._close(), loop=self._loop)

    async def _close(self):
        logging.info("{}".format(self))
        if self._state is not State.WaitClose:
            return 

        self._state = State.Closeing
        self._server.close()
        await self._server.wait_closed()
        self._server = None
        self._state = State.Null
        self._accept_cb.on_close()

    async def _listen(self):
        logging.info("{}".format(self))
        if self._state is not State.WaitListen:
            return 

        def factory():
            return CStreamProtocol(self._accept_cb)

        self._state = State.Listening
        self._server = await self._loop.create_server(
            factory, str(self._ip), self._port.value)
        self._state = State.Listened
        self._accept_cb.on_listen()
