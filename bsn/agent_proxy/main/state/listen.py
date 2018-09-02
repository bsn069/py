#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging
import importlib
import asyncio
state_mgr = importlib.import_module('{}_mgr'.format(__package__))
from . import _base
from bsn.common import tcp_server

class CState(_base.CState):
    """ 
    """
    C_strState = f_strFileBaseName

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))
        self.owner._CIP = self.app.config('ip')
        self.owner._CPort = self.app.config('port')
        asyncio.ensure_future(self.owner.start_listen(), loop = self.app.loop)
        self.to_state('run')

def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)
state_mgr.CStateMgr.reg_state(CState.C_strState, create_func)
file_import_tree.file_end(__name__)