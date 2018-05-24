#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import tcp_connect
 


class Portal(object):

    def __init__(self):
        self._host = "portal-dev.js.xoyo.com"
        self._port = 9262
        self._reader = None
        self._writer = None
        self._tcp_connect = tcp_connect.TCPConnect()

    async def run(self):
        self._tcp_connect.connect(self._host, self._port)
        await self._connect()
        # await self.connect(self._host, self._host)
        pass

    async def _connect(self):
        self._reader, self._writer = await asyncio.open_connection(self._host, self._port)
        # header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        # writer.write(header.encode('utf-8'))
        # await writer.drain()
        # while True:
        #     line = await reader.readline()
        #     if line == b'\r\n':
        #         break
        #     print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        #     # break
        # # Ignore the body, close the socket
        # writer.close()

    def send(self):
        self._writer.write()
        pass