#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging

class CStateMgr(object):
    """ 
    """
    
    '''
    bsn.agent.agent_proxy.state_enum.EState
    '''
    
    @classmethod
    def reg_state(cls, strState, funCreate):
        '''
        '''
        logging.info("{} strState={} {}".format(cls.__name__, strState, funCreate))
        cls.C_mapStateCreateFun[strState] = funCreate

    def __init__(self, oCOwner):
        """
        """
        logging.info("{} oCOwner={}".format(self, oCOwner))

        self._oCOwner = oCOwner
        self._oCStateCur = None

        self._oCState = {}
        for strState in self.C_mapStateCreateFun:
            funcCreate = self.C_mapStateCreateFun[strState]
            self._oCState[strState] = funcCreate(self)

    @property
    def state(self):
        return self._oCStateCur

    @property
    def owner(self):
        return self._oCOwner

    def to_state(self, strState):
        '''
        '''
        logging.info("{} strState={}".format(self, strState))
        oCAgentStateOld = self.state 
        oCAgentStateNew = self._oCState[strState]
        if oCAgentStateOld is oCAgentStateNew:
            return
        if oCAgentStateOld is not None:
            oCAgentStateOld._leave(oCAgentStateNew)
        self._oCStateCur = oCAgentStateNew
        oCAgentStateNew._enter(oCAgentStateOld)





file_import_tree.file_end(__name__)
