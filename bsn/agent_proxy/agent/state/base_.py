#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging


class CState(object):
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

    def enter(self):
        logging.info("{}".format(self))

    def leave(self):
        logging.info("{}".format(self))

    def on_recv_msg(self, oCMsg):
        logging.info("{} {}".format(self, oCMsg))
    

file_import_tree.file_end(__name__)