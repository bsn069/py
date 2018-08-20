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
        funSendData 
            def (byData):
        """
        self._CMsgForSend = msg.CMsg()
        self._funSendData = funSendData
        self._uSendPkgCount = 0
        self._uSendByteCount = 0

    def send_pkg(self, cmd, data):
        logging.info("{} cmd={}".format(self, cmd))
        self._uSendPkgCount = self._uSendPkgCount + 1
        self._CMsgForSend.cmd = cmd
        self._CMsgForSend.body = data
        byData = self._CMsgForSend.serialize()
        self._uSendByteCount = self._uSendByteCount + len(byData)
        self._funSendData(byData)

    def __str__(self):
        return 'CMsgSendPkg[pkg={} byte={}]'.format(self._uSendPkgCount, self._uSendByteCount)

file_import_tree.file_end(__name__)        
