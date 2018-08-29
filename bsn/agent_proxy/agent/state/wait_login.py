#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.agent_proxy.agent.state import base_
from bsn.agent_proxy.agent import state_enum
from bsn.agent_proxy.agent import state_mgr
from bsn.pb.agent2agentproxy import login_pb2
from bsn.pb.agent2agentproxy import cmd_pb2

class CState(base_.CState):
    """ 
    """
    C_EState = state_enum.EState.WaitLogin

    def __init__(self, oCAgent):
        """
        """
        logging.info("{}".format(self))
        super().__init__(oCAgent)

    def leave(self):
        logging.info("{}".format(self))

    def enter(self):
        logging.info("{}".format(self))

    def on_recv_msg(self, oCMsg):
        logging.info("{} {}".format(self, oCMsg))

        if oCMsg.cmd == cmd_pb2.EMsgId_Login:
            oMReq = login_pb2.MReq()
            oMReq.ParseFromString(oCMsg.body)
            logging.info("{} oMReq={}".format(self, oMReq))
            self.to_state(state_enum.EState.LoginSuccess)

def create_func(oCAgent):
    logging.info("{}".format(oCAgent))
    return CState(oCAgent)

state_mgr.CStateMgr.reg_state(CState.C_EState, create_func)

file_import_tree.file_end(__name__)