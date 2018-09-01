#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

class CStateMgr(object):
    """ 
    """
    
    '''
    bsn.agent.agent_proxy.state_enum.EState
    '''
    
    @classmethod
    def reg_state(cls, eEState, funCreate):
        '''
        eEState enum
        '''
        logging.info("{} eEState={} {}".format(cls.__name__, eEState, funCreate))
        cls.C_mapStateCreateFun[eEState.value] = funCreate

    def __init__(self, oCOwner):
        """
        """
        logging.info("{} oCOwner={}".format(self, oCOwner))

        self._oCOwner = oCOwner
        self._oCStateCur = None

        self._oCState = {}
        for uIndex in self.C_mapStateCreateFun:
            funcCreate = self.C_mapStateCreateFun[uIndex]
            self._oCState[uIndex] = funcCreate(self)

    @property
    def state(self):
        return self._oCStateCur

    @property
    def owner(self):
        return self._oCOwner

    def to_state(self, eEStateTo):
        '''
        '''
        logging.info("{} eEStateTo={}".format(self, eEStateTo))
        oCAgentStateOld = self.state 
        oCAgentStateNew = self._oCState[eEStateTo.value]
        if oCAgentStateOld is oCAgentStateNew:
            return
        if oCAgentStateOld is not None:
            oCAgentStateOld._leave(oCAgentStateNew)
        self._oCStateCur = oCAgentStateNew
        oCAgentStateNew._enter(oCAgentStateOld)





file_import_tree.file_end(__name__)
