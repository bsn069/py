#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging

class CStateOwner(object):
    """ 
    """

    def __init__(self, oCOwner, oCApp, u64CreateIndex):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={}".format(oCOwner, u64CreateIndex))
        self._oCOwner = oCOwner
        self._u64CreateIndex = u64CreateIndex
        self._u32Id = None
        self._oCStateMgr = None
        self._oCApp = oCApp

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
    def app(self):
        return self._oCApp

    @property
    def main(self):
        return self.app.main

    @property
    def id(self):
        '''
        return u32
        '''
        return self._u32Id

    def set_id(self, u32Id):
        self._u32Id = u32Id

    def to_state(self, strState):
        '''
        '''
        logging.info("strState={}".format(strState))
        self.state_mgr.to_state(strState)

    def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))
        self.state_mgr.state.on_recv_msg(u16Cmd, byData)

    # def send_pkg(self, u16Cmd, byData):
    #     logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))

    # def send_pb(self, u16Cmd, oPbMsg):
    #     logging.info("{} u16Cmd={} oPbMsg={}".format(self, u16Cmd, oPbMsg))

file_import_tree.file_end(__name__)