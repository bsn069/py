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


class CMsgParse(object):
    """ 
    """

    def __init__(self):
        """
        """
        logging.info("{}".format(self))

        self._byReadBuf = bytearray()
        self._bWaitHead = True
        self._uWaitLength = self._CMsg.head.Bit
        self._CMsg = msg.CMsg()

    def on_recv_msg(self, oCMsg):
        pass

    def _wait_head(self):
        self.on_recv_msg(self._CMsg)
        self._CMsg = msg.CMsg()
        self._bWaitHead = True
        self._uWaitLength = self._CMsg.head.Bit

    def _parse_head(self, data):
        self._CMsg.head.parse(data)
        if self._uWaitLength > 0:
            self._uWaitLength = self._CMsg.head.length
            self._bWaitHead = False
        else:
            self._wait_head()

    def _parse_body(self, data):
        self._CMsg.body = data
        self._wait_head()

    def proc_data(self, data):
        logging.info("{} type(data):{} {} len(data):{}".format(self, type(data), data, len(data)))
        uDataLength = len(data)
        uProcBegin = 0
        uLeftDataLength = uDataLength

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