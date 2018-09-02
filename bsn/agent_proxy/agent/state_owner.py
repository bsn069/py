#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging

from . import state_mgr
from bsn.common.state_mgr import base_state_owner
from bsn.common import tcp_session
# from ..sub_module import state_owner as sub_module

class CStateOwner(base_state_owner.CStateOwner, tcp_session.CTCPSession):
    """ 
    """

    def __init__(self, oCOwner, oCApp, u64CreateIndex):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={} ".format(oCOwner, u64CreateIndex))
        base_state_owner.CStateOwner.__init__(self, oCOwner, oCApp, u64CreateIndex)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        tcp_session.CTCPSession.__init__(self)

        self._u64SubModuleCreateIndex = 0
        self._listAgentProxy = []

    def connection_made(self, transport):
        logging.info("{} {}".format(self, transport))
        tcp_session.CTCPSession.connection_made(self, transport)
        self.to_state('connected')
       
    def connection_lost(self, exc):
        logging.info("{} {}".format(self, exc))
        self.to_state('disconnect')
        tcp_session.CTCPSession.connection_lost(self, exc)



file_import_tree.file_end(__name__)