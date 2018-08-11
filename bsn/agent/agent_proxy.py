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
        self.send_pkg(b"hello")

    def _on_dis_connect(self):
        logging.info("{}".format(self))