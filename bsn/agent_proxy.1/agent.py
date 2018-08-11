#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err

class EState(enum.Enum):
    Null = 0
    WaitConnect = 1
    Runing = 2
    WaitClose = 3

class CAgent(tcp_session.CTCPSession):
    """ 
    """

    def __init__(self, oCAgentProxy, uCreateIndex):
        """
        """
        logging.info("{}".format(self))
        super().__init__()

        self._CAgentProxy = oCAgentProxy
        self._uCreateIndex = uCreateIndex

    def connection_made(self, transport):
        logging.info("{} {}".format(self, transport))
        super().connection_made(transport)

    def connection_lost(self, exc):
        logging.info("{} {}".format(self, exc))
        super().connection_lost(exc)
        self._CAgentProxy = None

    def data_received(self, data):
        logging.info("{} {}".format(self, data))
        self._read_buff.append(data)
