#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging


class CState(object):
    """ 
    """

    C_strState = f_strFileBaseName

    def __init__(self, oCStateMgr):
        """
        oCStateMgr CStateMgr
        """
        logging.info("oCStateMgr={}".format(oCStateMgr))
        self._oCStateMgr = oCStateMgr

    @property
    def state_mgr(self):
        return self._oCStateMgr

    @property
    def owner(self):
        return self.state_mgr.owner

    @property
    def app(self):
        return self.owner.app

    @property
    def main(self):
        return self.owner.main

    def to_state(self, strState):
        '''
        '''
        logging.info("strState={}".format(strState))
        self.state_mgr.to_state(strState)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))

    def _leave(self, oCStateNext):
        logging.info("{} oCStateNext={}".format(self, oCStateNext))

    def on_recv_msg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={}".format(self, u16Cmd))

    def get_pb(self, cls, byData):
        oPBMsg = cls()
        if byData is not None:
            oPBMsg.ParseFromString(byData)
        logging.info("{} cls={} oPBMsg={}".format(self, cls, oPBMsg))
        return oPBMsg

    def send_pkg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))
        return self.owner.send_pkg(u16Cmd, byData)

    def send_pb(self, u16Cmd, oPbMsg):
        logging.info("{} u16Cmd={} oPbMsg={}".format(self, u16Cmd, oPbMsg))
        return self.owner.send_pb(u16Cmd, oPbMsg)

file_import_tree.file_end(__name__)