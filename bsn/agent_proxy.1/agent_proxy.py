#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import asyncio
from bsn.common.ip_port import CIPPort
from bsn.common.ip import CIP
from bsn.common.port import CPort
from bsn.common import tcp_accept
from bsn.common import err
from bsn.common import tcp_server
import logging
from bsn.agent_proxy import agent
import enum

class CAgentProxy(tcp_server.CTCPServer):

    def __init__(self, loop):
        logging.info("{}".format(self))

        super().__init__(loop)

        self._Index2CAgent = {}
        self._uCreateIndex = 0

    def getAgentByCreateIndex(self, uCreateIndex):
        return self._Index2CAgent[uCreateIndex]

    def _parse_arg(self):
        logging.info("{}".format(self))

        self._CIP = CIP('0.0.0.0')
        self._CPort = CPort(10001)

    def _create_session(self):
        '''
        tcp_session.CTCPSession()
        '''
        logging.info("{}".format(self))
        self._uCreateIndex = self._uCreateIndex + 1
        oCAgent = agent.CAgent(self, self._uCreateIndex)
        self._Index2CAgent[self._uCreateIndex] = oCAgent
        return oCAgent

    def _on_tcp_start_listen(self):
        logging.info("{}".format(self))
        super()._on_tcp_start_listen()

    def _on_tcp_stop_listen(self):
        logging.info("{}".format(self))

        super()._on_tcp_stop_listen()



