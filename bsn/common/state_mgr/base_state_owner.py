#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

class CStateOwner(object):
    """ 
    """

    def __init__(self, oCOwner, u64CreateIndex = 0, u32Id = 0):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={} u32Id={}".format(oCOwner, u64CreateIndex, u32Id))
        self._oCOwner = oCOwner
        self._u64CreateIndex = u64CreateIndex
        self._u32Id = u32Id
        self._oCStateMgr = None

    @property
    def create_index(self):
        return self._u64CreateIndex

    @property
    def state_mgr(self):
        return self._oCStateMgr

    @property
    def owner(self):
        return self._oCOwner

    @property
    def id(self):
        '''
        return u32
        '''
        return self._u32Id

    def to_state(self, eEStateTo):
        '''
        eEStateTo state_enum.EState.
        '''
        logging.info("eEStateTo={}".format(eEStateTo))
        self.state_mgr.to_state(eEStateTo)

    def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))
        self.state_mgr.state.on_recv_msg(u16Cmd, byData)

    def send_pkg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))

    def send_pb(self, u16Cmd, oPbMsg):
        logging.info("{} u16Cmd={} oPbMsg={}".format(self, u16Cmd, oPbMsg))

file_import_tree.file_end(__name__)