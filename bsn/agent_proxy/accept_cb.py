#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import logging
from bsn.common import err
from bsn.common import tcp_accept
from bsn.agent_proxy import stream_protocol

class CTCPAcceptCB(tcp_accept.CTCPAcceptCB):
    '''
    '''
    def __init__(self, oCAgentProxy):
        '''
        '''
        logging.info("{}".format(self))
        super().__init__()
        self._oCAgentProxy = oCAgentProxy 

    def create_stream_protocal(self):
        '''
        return CStreamProtocol
        '''
        logging.info("{}".format(self))
        return stream_protocol.CStreamProtocol(self)

    def on_connect(self, oCStreamProtocol):
        """
        """
        logging.info("{}".format(self))
        self._oCAgentProxy.on_connect(oCStreamProtocol)

    def on_listen(self):
        logging.info("{}".format(self))
        self._oCAgentProxy.on_listen()

    def on_close(self):
        logging.info("{}".format(self))
        self._oCAgentProxy.on_close()
