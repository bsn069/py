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

    def __init__(self, oOwner):
        """
        oOwner CAgentProxy
        """
        logging.info("{}".format(self))
        self._oOwner = oOwner 

    @property
    def owner(self):
        return self._oOwner

    @property
    def state_mgr(self):
        return self.owner.state_mgr

    def to_state(self, EState_To):
        '''
        EState_To state_enum.EState.
        '''
        self.owner.to_state(EState_To)

    def enter(self):
        logging.info("{}".format(self))

    def leave(self):
        logging.info("{}".format(self))

    def on_recv_msg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={}".format(self, u16Cmd))
    

file_import_tree.file_end(__name__)