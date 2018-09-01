#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import logging
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.common.state_mgr import base_state
from bsn.common.port import CPort
from bsn.common.host import CHost

class CState(base_state.CState):
    """ 
    """
    C_eEState = state_enum.EState.WaitConnect

    def __init__(self, oOwner):
        """
        """
        super().__init__(oOwner)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))
        self.owner.set_host_port(CHost('127.0.0.1'), CPort(10001))
        asyncio.ensure_future(self.connect(), loop=self.owner.loop)

    async def connect(self):
        await self.owner.connect()
        self.to_state(state_enum.EState.Login)

def create_func(oCOwner):
    logging.info("{}".format(oCOwner))
    return CState(oCOwner)
state_mgr.CStateMgr.reg_state(CState.C_eEState, create_func)
file_import_tree.file_end(__name__)