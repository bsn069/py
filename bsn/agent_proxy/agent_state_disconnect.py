#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err
from bsn.agent_proxy import agent_state
 

class CAgentState(agent_state.CAgentState):
    """ 
    """

    def __init__(self, oCAgent):
        """
        """
        logging.info("{}".format(self))
        super().__init__(oCAgent)

    def leave(self):
        logging.info("{}".format(self))

    def enter(self):
        logging.info("{}".format(self))

    def proc_pkg(self, byPkg):
        logging.info("{} {}".format(self, byPkg))
    
 
