#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging
import importlib
state_mgr = importlib.import_module('{}_mgr'.format(__package__))
from . import _base

from bsn.pb.agent_agentproxy import trans_pb2
from bsn.pb.agent_agentproxy import cmd_pb2

class CState(_base.CState):
    """ 
    """
    C_strState = f_strFileBaseName

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)

    def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))

        if u16Cmd == cmd_pb2.EMsgId2Agent_FromAgent:
            oM2Agent_FromAgent = self.get_pb(trans_pb2.M2Agent_FromAgent, byData)
            logging.info("oM2Agent_FromAgent={}".format(oM2Agent_FromAgent))



def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)
state_mgr.CStateMgr.reg_state(CState.C_strState, create_func)
file_import_tree.file_end(__name__)