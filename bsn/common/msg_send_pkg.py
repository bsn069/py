#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.common.port import CPort
from bsn.common.ip import CIP
from bsn.common import err
from bsn.common import msg



class CMsgSendPkg(object):
    """ 
    """

    def __init__(self, funSendData):
        """
        in
            funSendData function
                def (byte):
        """
        logging.info("1{} ".format(self))
        self._CMsgForSend = msg.CMsg()
        logging.info("2{} ".format(self))
        self._funSendData = funSendData
        self._uSendPkgCount = 0
        self._uSendByteCount = 0

    def send_pkg(self, cmd, data):
        '''
        in 
            cmd     int 
                command
            data    byte 
        ret
            bool 
                is send ok
        '''
        logging.info("{} cmd={} data={}".format(self, cmd, data))
        self._uSendPkgCount = self._uSendPkgCount + 1
        self._CMsgForSend.cmd = cmd
        self._CMsgForSend.body = data
        byData = self._CMsgForSend.serialize()
        self._uSendByteCount = self._uSendByteCount + len(byData)
        return self._funSendData(byData)

    def send_pb(self, u16Cmd, oPbMsg):
        logging.info("{} u16Cmd={} oPbMsg={}".format(self, u16Cmd, oPbMsg))
        byOut = oPbMsg.SerializeToString()
        self.send_pkg(u16Cmd, byOut)
        
    # def __str__(self):
    #     return 'CMsgSendPkg[pkg={} byte={}]'.format(self._uSendPkgCount, self._uSendByteCount)

file_import_tree.file_end(__name__)        
