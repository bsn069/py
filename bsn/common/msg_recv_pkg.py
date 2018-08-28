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
from bsn.common import msg


class CMsgRecvPkg(object):
    """ 
    """

    def __init__(self, funOnRecvMsg):
        """
        funOnRecvMsg
            def (msg.CMsg())
        """
        logging.info("{}".format(self))

        self._byReadBuf = bytearray()
        self._bWaitHead = True
        self._CMsg = msg.CMsg()
        self._uWaitLength = self._CMsg.head.Bit
        self._funOnRecvMsg = funOnRecvMsg
        self._uRecvPkgCount = 0
        self._uRecvByteCount = 0

    def _wait_head(self):
        self._funOnRecvMsg(self._CMsg)
        self._CMsg = msg.CMsg()
        self._bWaitHead = True
        self._uWaitLength = self._CMsg.head.Bit

    def _parse_head(self, data):
        logging.info("{} {}".format(self, data))
        self._uRecvPkgCount = self._uRecvPkgCount + 1
        self._CMsg.head.parse(data)
        if self._CMsg.head.length > 0:
            self._uWaitLength = self._CMsg.head.length
            self._bWaitHead = False
        else:
            self._wait_head()

    def _parse_body(self, data):
        self._CMsg.body = data
        self._wait_head()

    # def __str__(self):
    #     return 'CMsgRecvPkg[pkg={} byte={}]'.format(self._uRecvPkgCount, self._uRecvByteCount)

    def proc_data(self, data):
        logging.info("{} type(data):{} {} len(data):{}".format(self, type(data), data, len(data)))
        uDataLength = len(data)
        uProcBegin = 0
        uLeftDataLength = uDataLength
        self._uRecvByteCount = self._uRecvByteCount + uDataLength

        while uLeftDataLength > 0:
            if uLeftDataLength >= self._uWaitLength:
                byProcData = data[uProcBegin : uProcBegin + self._uWaitLength]
                uProcBegin = uProcBegin + self._uWaitLength
                if len(self._byReadBuf) > 0:
                    self._byReadBuf.extend(byProcData)
                    byProcData = bytes(self._byReadBuf)
                    self._byReadBuf.clear()

                if self._bWaitHead:
                    self._parse_head(byProcData)
                else:
                    self._parse_body(byProcData)
            else:
                byProcData = data[uProcBegin : uProcBegin + uLeftDataLength]
                self._byReadBuf.extend(byProcData)
                self._uWaitLength = self._uWaitLength - uLeftDataLength
                break
            uLeftDataLength = uDataLength - uProcBegin
        
file_import_tree.file_end(__name__)