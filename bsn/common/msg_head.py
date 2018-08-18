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

    def __init__(self):
        """
        """
        logging.info("{}".format(self))
        self._length = 0
        self._id = 0

    @property
    def id(self):
        return self._id
        
    @property
    def id(self):
        return self._id

    def connection_made(self, transport):
        logging.info("{}".format(self))
        self._transport = transport
        self._EStateCTCPSession = EState.Connected

    def connection_lost(self, exc):
        logging.info("{}".format(self))
        self._EStateCTCPSession = EState.DisConnected

    def data_received(self, data):
        logging.info("{} {}".format(self, data))
        self._read_buff.append(data)

    def eof_received(self):
        logging.info("{}".format(self))

    def write(self, data):
        logging.info("{} {}".format(self, data))
        self._write_buff.append(data)

    def flush(self):
        self._transport.write(self._write_buff)

    def read(self):
        return self._read_buff

    def close(self):
        return self._transport.close()
        
file_import_tree.file_end(__name__)