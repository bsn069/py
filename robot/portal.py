#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio



class Portal(object):

    def __init__(self):
        self._Host = "portal-dev.js.xoyo.com"
        self._Port = 9262

    async def run(self):
        await self.connect("www.163.com")
        # await self.connect(self._Host, self._Port)
        pass

    async def connect(self, host, port = 80):
        reader, writer = await asyncio.open_connection(host, port)
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        await writer.drain()
        while True:
            line = await reader.readline()
            if line == b'\r\n':
                break
            print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
            # break
        # Ignore the body, close the socket
        writer.close()