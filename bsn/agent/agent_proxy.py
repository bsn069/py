#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_client
from bsn.common import err
from bsn.common.port import CPort
from bsn.common.host import CHost

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
        self._uIndex = oCAgent.gen_agent_proxy_index()

    @property
    def index(self):
        return self._uIndex

    async def run(self):
        logging.info("{}".format(self))

        self._CHost = CHost('127.0.0.1')
        self._CPort = CPort(10001)

        uLoopCount = 0
        while uLoopCount < 3:
            uLoopCount = uLoopCount + 1
            if self.estate_tcp_client() != tcp_client.EState.Connected:
                await self.connect()
            strSendPkg = '{}_{}_pkg'.format(self.index, uLoopCount)
            self.send_pkg(strSendPkg.encode())
            await asyncio.sleep(1)
        await self.disconnect("client close")

        logging.info('leave {}'.format(self))

    async def _on_recv_pkg(self, byData):
        logging.info("{} byData:{}".format(self, byData))
        await super()._on_recv_pkg(byData)