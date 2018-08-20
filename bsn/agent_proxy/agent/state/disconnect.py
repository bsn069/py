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

class CState(base_.CState):
    """ 
    """
    C_EState = state_enum.EState.DisConnect

    def __init__(self, oCAgent):
        """
        """
        logging.info("{}".format(self))
        super().__init__(oCAgent)

    def leave(self):
        logging.info("{}".format(self))

    def enter(self):
        logging.info("{}".format(self))


def create_func(oCAgent):
    logging.info("{}".format(oCAgent))
    return CState(oCAgent)

state_mgr.CStateMgr.reg_state(CState.C_EState, create_func)

file_import_tree.file_end(__name__)