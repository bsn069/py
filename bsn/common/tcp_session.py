#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common.port import CPort
from bsn.common.ip import CIP
from bsn.common import err

class CTCPSession(asyncio.protocols.Protocol):
    """ 
    """

    def __init__(self):
        """
        """
        logging.info("{}".format(self))
        self._transport = None
        self._read_buff = bytearray()
        self._write_buff = bytearray()

    def connection_made(self, transport):
        logging.info("{}".format(self))
        self._transport = transport

    def connection_lost(self, exc):
        logging.info("{}".format(self))

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
        
