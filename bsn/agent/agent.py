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
        self._uAgentProxyIndex = 0

    async def run(self):
        logging.info("{}".format(self))

        oCAgentProxy = CAgentProxy(self, self._loop)
        asyncio.ensure_future(oCAgentProxy.run(), loop = self._loop)

        oCAgentProxy = CAgentProxy(self, self._loop)
        asyncio.ensure_future(oCAgentProxy.run(), loop = self._loop)

        oCAgentProxy = CAgentProxy(self, self._loop)
        asyncio.ensure_future(oCAgentProxy.run(), loop = self._loop)

        oCAgentProxy = CAgentProxy(self, self._loop)
        await oCAgentProxy.run()

        logging.info("leave {}".format(self))

    def gen_agent_proxy_index(self):
        self._uAgentProxyIndex = self._uAgentProxyIndex + 1
        return self._uAgentProxyIndex