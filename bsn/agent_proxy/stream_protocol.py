#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_accept
from bsn.common import err

class CStreamProtocol(tcp_accept.CStreamProtocol):
    """ 
    """

    def __init__(self, accept_cb):
        """
        """
        logging.info("{}".format(self))
        super().__init__(accept_cb)

    def connection_lost(self, exc):
        logging.info("{} {}".format(self, exc))

    def data_received(self, data):
        logging.info("{} {}".format(self, data))

    def eof_received(self):
        logging.info("{}".format(self))

