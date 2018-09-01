#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.agent.agent_proxy.state import _base

from bsn.pb.agent2agentproxy import login_pb2
from bsn.pb.agent2agentproxy import cmd_pb2
 
class CState(_base.CState):
    """ 
    """
    C_strState = f_strFileBaseName

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))

        oMReq = login_pb2.MReq()
        oMReq.id = self.owner.owner.id
        logging.info("{} self.owner.owner.id={}".format(self, self.owner.owner.id))
        self.send_pb(cmd_pb2.EMsgId_Login, oMReq) 


    async def connect(self):
        await self.owner.connect()
        self.to_state(state_enum.EState.Login)

def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)
state_mgr.CStateMgr.reg_state(CState.C_strState, create_func)
file_import_tree.file_end(__name__)