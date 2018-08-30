#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

from bsn.common.state_mgr.example import state_enum
from bsn.common.state_mgr.example import state_mgr
from bsn.common.state_mgr import base_state_owner

class CStateOwner(base_state_owner.CStateOwner):
    """ 
    """

    def __init__(self, oCOwner, u64CreateIndex = 0, u32Id = 0):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={} u32Id={}".format(oCOwner, u64CreateIndex, u32Id))
        base_state_owner.CStateOwner.__init__(self, oCOwner, u64CreateIndex = u64CreateIndex, u32Id=u32Id)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        # self.to_state(state_enum.EState.Init)



file_import_tree.file_end(__name__)