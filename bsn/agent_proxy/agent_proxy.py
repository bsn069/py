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
from bsn.agent_proxy import accept_cb
import enum

class CAgentProxy(tcp_server.CTCPServer):

    def __init__(self, loop):
        logging.info("{}".format(self))

        oCTCPAcceptCB = accept_cb.CTCPAcceptCB(self)
        super().__init__(loop, oCTCPAcceptCB)

    def _parse_arg(self):
        logging.info("{}".format(self))

        self._CIP = CIP('0.0.0.0')
        self._CPort = CPort(10001)

    def on_connect(self, oCStreamProtocol):
        """
        """
        logging.info("{}".format(self))

    def on_listen(self):
        logging.info("{}".format(self))
        super().on_listen()

    def on_close(self):
        logging.info("{}".format(self))
        super().on_close()

