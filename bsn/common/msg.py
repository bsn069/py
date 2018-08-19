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
from bsn.common import msg_head

class CMsg(object):
    """ 
    """

    def __init__(self):
        """
        """
        # logging.info("{}".format(self))
        self._CMsgHead = msg_head.CMsgHead()
        self._byBody = None

    @property
    def head(self):
        return self._CMsgHead

    @property
    def cmd(self):
        return self.head.cmd

    @cmd.setter
    def cmd(self, v):
        self.head.cmd = v

    @property
    def body(self):
        return self._byBody

    @body.setter
    def body(self, v):
        self._byBody = v
        self.head.length = len(v)

    def __str__(self):
        return 'head=[{}] body=[{}]'.format(self.head, self.body)

    def serialize(self):
        '''
        return byte
        '''
        logging.info("{} ".format(self))

        byBuf = bytearray()

        byTmp = self.head.serialize()
        byBuf.extend(byTmp)
        if self.body is not None:
            byBuf.extend(self.body)

        return bytes(byBuf)

    def parse(self, data):
        logging.info("{} type(data):{} {} len(data):{}".format(self, type(data), data, len(data)))
        self.head.parse(data)
        uTotalLength = self.head.Bit + self.head.length
        self.body = data[self.head.Bit:uTotalLength]
        return uTotalLength


file_import_tree.file_end(__name__)