#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import session
 


class Test(object):

    def __init__(self, loop):
        self._loop = loop
        self._host = "localhost"
        self._port = 9262

    async def run(self):
        await session.connect(self._host, self._port, self._loop)
 

