#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err

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
