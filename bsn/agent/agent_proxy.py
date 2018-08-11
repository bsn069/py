#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_client
from bsn.common import err

class EState(enum.Enum):
    Null = 0
    WaitConnect = 1
    Runing = 2
    WaitClose = 3

class CAgentProxy(tcp_client.CTCPClient):
    """ 
    """

    def __init__(self, oCAgent, loop):
        """
        """
        logging.info("{}".format(self))
        super().__init__(loop)

        self._CAgent = oCAgent

    def _on_connect(self):
        logging.info("{}".format(self))
        asyncio.ensure_future(self._run(), loop=self._loop)

    def _on_dis_connect(self):
        logging.info("{}".format(self))
        super()._on_connect_fail()

    async def _run(self):
        logging.info("{}".format(self))
        while self._EStateCTCPClient == tcp_client.EState.Connected:
            self.send_pkg(b"hello")
            await asyncio.sleep(3)
            self.send_pkg(b"world!")
            await asyncio.sleep(3)
