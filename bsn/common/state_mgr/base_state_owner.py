#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

class CStateOwner(object):
    """ 
    """

    def __init__(self, oCOwner):
        """
        """
        logging.info("oCOwner={}".format(oCOwner))
        self._oCOwner = oCOwner
        self._oCStateMgr = None

    async def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        await self.state_mgr.on_recv_msg(u16Cmd, byData)

    @property
    def state_mgr(self):
        return self._oCStateMgr

    @property
    def owner(self):
        return self._oCOwner

    def to_state(self, eEStateTo):
        '''
        eEStateTo state_enum.EState.
        '''
        self.state_mgr.to_state(eEStateTo)


file_import_tree.file_end(__name__)