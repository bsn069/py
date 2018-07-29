#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
import socket


class Session(object):
    """  
    """

    def __init__(self, reader, writer):
        logging.info("{}".format(self))
        self._reader = reader
        self._writer = writer

    def send(self, data):
        self.write_bytes(data)

    def close(self):
        logging.info("{}".format(self))
        if self._writer:
            self._writer.transport.close()
        self._writer = None
        self._reader = None

    def is_close(self):
        return self._writer is None

    async def read_bytes(self, num_bytes):
        data = await self._reader.readexactly(num_bytes)
        return data

    def write_bytes(self, data):
        return self._writer.write(data)

    async def wait_all_send(self):
        await self._writer.drain()

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


async def connect(host, port, loop):
    """
    return Session()
    """
    logging.info("{} {}".format(host, port))
    _reader, _writer = await asyncio.open_connection(host, port, loop=loop)
    _session = Session(_reader, _writer)
    return _session
