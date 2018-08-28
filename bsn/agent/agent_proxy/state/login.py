#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.agent.agent_proxy.state import base_
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.common.port import CPort
from bsn.common.host import CHost

class CState(base_.CState):
    """ 
    """
    C_EState = state_enum.EState.Login

    def __init__(self, oOwner):
        """
        """
        super().__init__(oOwner)

    def enter(self):
        logging.info("{}".format(self))
        self.send_pkg(1, b'')


    def leave(self):
        logging.info("{}".format(self))


def create_func(oOwner):
    logging.info("{}".format(oOwner))
    return CState(oOwner)

state_mgr.CStateMgr.reg_state(CState.C_EState, create_func)

file_import_tree.file_end(__name__)