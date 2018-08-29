#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
from bsn.common.ip_port import CIPPort
from bsn.common.ip import CIP
from bsn.common.port import CPort
from bsn.common import tcp_accept
from bsn.common import err
from bsn.common import tcp_server
import logging
from bsn.agent.agent_proxy import agent_proxy

from bsn.pb import comm_pb2

class CAgent(object):

    def __init__(self, loop):
        logging.info("{}".format(self))

        self._loop = loop
        self._Index2CAgentProxy = {}
        self._uCreateIndex = 0
        self._u32Id = 1

    @property
    def id(self):
        '''
        return u32
        '''
        return self._u32Id

    def _create_agent_proxy(self):
        '''
        '''
        logging.info("{}".format(self))
        self._uCreateIndex = self._uCreateIndex + 1
        oCAgentProxy = agent_proxy.CAgentProxy(self, self._uCreateIndex)
        self._Index2CAgentProxy[self._uCreateIndex] = oCAgentProxy
        return oCAgentProxy

    async def _run(self):
        file_import_tree.file_print()
        logging.info("{}".format(self))

        self._create_agent_proxy()
        while True:
            await asyncio.sleep(1)

    async def run(self):
        logging.info("{}".format(self))
        await self._run()

    @property
    def loop(self):
        return self._loop
        

file_import_tree.file_end(__name__)
