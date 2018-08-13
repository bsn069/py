#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err
 

class CAgentState(object):
    """ 
    """

    def __init__(self, oCAgent):
        """
        """
        logging.info("{}".format(self))
        self._CAgent = oCAgent 

    @property
    def agent(self):
        return self._CAgent

    def to_state(self, EState_To):
        self.agent.state_mgr.to_state(EState_To)

    def leave(self):
        logging.info("{}".format(self))

    def enter(self):
        logging.info("{}".format(self))

    def proc_pkg(self, byPkg):
        logging.info("{} {}".format(self, byPkg))
    
 
