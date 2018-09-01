#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging


class CState(object):
    """ 
    """

    C_eEState = None

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

    def to_state(self, eEStateTo):
        '''
        eEStateTo state_enum.EState.
        '''
        logging.info("eEStateTo={}".format(eEStateTo))
        self.state_mgr.to_state(eEStateTo)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))

    def _leave(self, oCStateNext):
        logging.info("{} oCStateNext={}".format(self, oCStateNext))

    def on_recv_msg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={}".format(self, u16Cmd))

    def send_pkg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))
        return self.owner.send_pkg(u16Cmd, byData)

    def send_pb(self, u16Cmd, oPbMsg):
        logging.info("{} u16Cmd={} oPbMsg={}".format(self, u16Cmd, oPbMsg))
        return self.owner.send_pb(u16Cmd, oPbMsg)

file_import_tree.file_end(__name__)