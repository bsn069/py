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
 

class CMsgHead(object):
    """ 
    """
    LengthBit = 2
    CmdBit = 2
    Bit = LengthBit + CmdBit

    def __init__(self):
        """
        """
        # logging.info("{}".format(self))
        self._length = 0
        self._cmd = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, v):
        self._length = v
        
    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, v):
        self._cmd = v

    def __str__(self):
        return 'cmd={} length={}'.format(self.cmd, self.length)

    def serialize(self):
        '''
        return byte
        '''
        logging.info("{} ".format(self))

        byBuf = bytearray()

        byTmp = self.length.to_bytes(self.LengthBit, byteorder='little')
        byBuf.extend(byTmp)

        byTmp = self.cmd.to_bytes(self.CmdBit, byteorder='little')
        byBuf.extend(byTmp)

        return bytes(byBuf)

    def parse(self, byData):
        logging.info("{} ".format(self))

        uIndex = 0

        uIndexEnd = uIndex + self.LengthBit
        self._length = int.from_bytes(byData[uIndex:uIndexEnd], 'little')
        uIndex = uIndexEnd

        uIndexEnd = uIndex + self.CmdBit
        self._cmd = int.from_bytes(byData[uIndex:uIndexEnd], 'little')
        uIndex = uIndexEnd


file_import_tree.file_end(__name__)