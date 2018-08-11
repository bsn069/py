#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err
from bsn.common import app
from bsn.agent.agent_proxy import CAgentProxy

from bsn.common.port import CPort
from bsn.common.host import CHost

class EState(enum.Enum):
    Null = 0
    WaitConnect = 1
    Runing = 2
    WaitClose = 3

class CAgent(app.CApp):
    """ 
    """

    def __init__(self, loop):
        """
        """
        logging.info("{}".format(self))
        super().__init__()

        self._loop = loop
        self._CAgentProxy = []

    def run(self):
        logging.info("{}".format(self))
        asyncio.ensure_future(self._run(), loop=self._loop)

    def stop(self):
        logging.info("{}".format(self))
        self._loop.stop()

    async def _run(self):
        logging.info("{}".format(self))
        self._connect_agent_proxy()

    def _connect_agent_proxy(self):
        logging.info("{}".format(self))
        oCAgentProxy = CAgentProxy(self, self._loop)
        self._CAgentProxy.append(oCAgentProxy)
        host = CHost("127.0.0.1")
        port = CPort(10001)
        oCAgentProxy.start_connect(host, port)

