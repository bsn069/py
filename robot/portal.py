#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import session
 


class Portal(object):

    def __init__(self, loop):
        self._loop = loop
        self._host = "10.11.131.102"
        self._port = 9252

    async def run(self):
        await session.connect(self._host, self._port, self._loop)
 

