#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)


import logging
from bsn.agent.agent import state_enum
from bsn.agent.agent_proxy import state_enum as agent_proxy_state_enum
from bsn.agent.agent import state_mgr
from bsn.common.state_mgr import base_state

class CState(base_state.CState):
    """ 
    """
    C_eEState = state_enum.EState.Run

    def __init__(self, oOwner):
        """
        """
        super().__init__(oOwner)
        self._listAgentProxy = []

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))
        oCStateOwnerAgentProxy = self.owner.create_agent_proxy()
        self._listAgentProxy.append(oCStateOwnerAgentProxy)
        oCStateOwnerAgentProxy.to_state(agent_proxy_state_enum.EState.Init)
        
        
def create_func(oCOwner):
    logging.info("{}".format(oCOwner))
    return CState(oCOwner)
state_mgr.CStateMgr.reg_state(CState.C_eEState, create_func)
file_import_tree.file_end(__name__)