#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)


import logging
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.common.state_mgr import base_state
from bsn.pb.agent2agentproxy import login_pb2
from bsn.pb.agent2agentproxy import cmd_pb2

class CState(base_state.CState):
    """ 
    """
    C_eEState = state_enum.EState.Login

    def __init__(self, oOwner):
        """
        """
        super().__init__(oOwner)


    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))

        oMReq = login_pb2.MReq()
        oMReq.id = self.owner.owner.id
        self.send_pb(cmd_pb2.EMsgId_Login, oMReq) 

def create_func(oCOwner):
    logging.info("{}".format(oCOwner))
    return CState(oCOwner)
state_mgr.CStateMgr.reg_state(CState.C_eEState, create_func)
file_import_tree.file_end(__name__)