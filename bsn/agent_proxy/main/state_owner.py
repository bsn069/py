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

from ..sub_module import state_owner as sub_module

class CStateOwner(base_state_owner.CStateOwner):
    """ 
    """

    def __init__(self, oCOwner, u64CreateIndex = 0, oCApp = None):
        """
        """
        u32Id = 1
        logging.info("oCOwner={} u64CreateIndex={} u32Id={}".format(oCOwner, u64CreateIndex, u32Id))
        base_state_owner.CStateOwner.__init__(self, oCOwner, u64CreateIndex = u64CreateIndex, u32Id=u32Id, oCApp = oCApp)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        self._u64SubModuleCreateIndex = 0
        self._listAgentProxy = []

    def send_pkg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))

    def send_pb(self, u16Cmd, oPbMsg):
        logging.info("{} u16Cmd={} oPbMsg={}".format(self, u16Cmd, oPbMsg))

    def create_module_sub(self):
        '''
        '''
        logging.info("{}".format(self))
        self._u64SubModuleCreateIndex = self._u64SubModuleCreateIndex + 1
        oModule = sub_module.CStateOwner(self, self._u64SubModuleCreateIndex, oCApp=self.app)
        self._listAgentProxy.append(oModule)
        return  oModule

file_import_tree.file_end(__name__)