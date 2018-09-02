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
from bsn.agent_proxy.agent import agent

from bsn.pb import comm_pb2

class CAgentProxy(tcp_server.CTCPServer):

    def __init__(self, loop):
        logging.info("{}".format(self))

        super().__init__(loop)

        self._Index2CAgent = {}
        self._uCreateIndex = 0

    def getAgentByCreateIndex(self, uCreateIndex):
        return self._Index2CAgent[uCreateIndex]

    def _create_session(self):
        '''
        tcp_session.CTCPSession()
        '''
        logging.info("{}".format(self))
        self._uCreateIndex = self._uCreateIndex + 1
        oCAgent = agent.CAgent(self, self._uCreateIndex)
        self._Index2CAgent[self._uCreateIndex] = oCAgent
        return oCAgent
 
    async def _run(self):
        file_import_tree.file_print()
        logging.info("{}".format(self))

        oMTest = comm_pb2.MTest()
        oMTest.id = 1
        oMTest.name = 'abc'
        print(oMTest)
        byOut = oMTest.SerializeToString()
        print(byOut)
        oMTest2 = comm_pb2.MTest()
        oMTest2.ParseFromString(byOut)
        print(oMTest2)

        while True:
            await asyncio.sleep(1)
            # logging.info("{}".format(self))
            for uIndex in self._Index2CAgent:
                # logging.info("{}".format(self))
                self._Index2CAgent[uIndex]._update()

file_import_tree.file_end(__name__)
