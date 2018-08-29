#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging


class CState(object):
    """ 
    """

    C_eEState = None

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