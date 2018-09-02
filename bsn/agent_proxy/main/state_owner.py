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

from ..agent import state_owner as agent
from bsn.common import tcp_accept

class CStateOwner(base_state_owner.CStateOwner, tcp_accept.CTCPAccept):
    """ 
    """

    def __init__(self, oCOwner, u64CreateIndex = 0, oCApp = None):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={}".format(oCOwner, u64CreateIndex))
        base_state_owner.CStateOwner.__init__(self, oCOwner, u64CreateIndex = u64CreateIndex, oCApp = oCApp)
        tcp_accept.CTCPAccept.__init__(self, self.app.loop)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        self._u64SubModuleCreateIndex = 0
        self._listAgentProxy = []

    def _create_session(self):
        '''
        '''
        logging.info("{}".format(self))
        self._u64SubModuleCreateIndex = self._u64SubModuleCreateIndex + 1
        oModule = agent.CStateOwner(self, self._u64SubModuleCreateIndex, oCApp=self.app)
        self._listAgentProxy.append(oModule)
        return  oModule

file_import_tree.file_end(__name__)