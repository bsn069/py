#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging


class State(enum.Enum):
    Null = 0
    Connecting = 1
    Connected = 2


class StreamProtocol(asyncio.protocols.Protocol):
    """ for loop.create_connection
    """

    def __init__(self, cb):
        self._cb = cb

    def connection_made(self, transport):
        logging.info("connection_made")
        self._cb.on_connect(transport)

    def connection_lost(self, exc):
        logging.info("connection_lost")
        self._cb.on_disconnect(exc)

    def data_received(self, data):
        logging.info("data_received")
        self._cb.on_recv(data)

    def eof_received(self):
        logging.info("eof_received")


class TCPConnect(object):
    """  
    """

    def __init__(self, loop=None):
        if loop is None:
            loop = asyncio.events.get_event_loop()
        self._loop = loop
        self._host = None
        self._port = None
        self._state = State.Null
        self._transport = None

    def connect(self, host, port):
        if self._state is not State.Null:
            return False
        self._host = host
        self._port = port
        self._state = State.Connecting
        asyncio.ensure_future(self._connect(), loop=self._loop)
        return True

    def close(self):
        if self._state is State.Null:
            return False
        self._transport.close()
        self._transport = None
        return True

    def dealy_close(self, sec):
        asyncio.ensure_future(self._dealy_close(1), loop=self._loop)

    def is_connected(self):
        return self._state == State.Connected

    def on_connect(self, transport):
        logging.info("on_connect")
        self._state = State.Connected
        # self._transport = transport
        self.dealy_close(1)

    def on_disconnect(self, exc):
        logging.info("on_disconnect")
        logging.info(exc)
        self._state = State.Null
        # self._transport = None

    def on_recv(self, data):
        logging.info("on_recv")

    async def _connect(self):
        stream_portocal = StreamProtocol(self)
        self._transport, _ = await self._loop.create_connection(
            lambda: stream_portocal, self._host, self._port)

    async def _dealy_close(self, sec):
        await asyncio.sleep(sec)
        self.close()
