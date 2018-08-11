#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common.port import CPort
from bsn.common.ip import CIP
from bsn.common import err

class EState(enum.Enum):
    Null = 0
    Connected = 1
    DisConnected = 2


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
        self._EStateCTCPSession = EState.Null

    @property
    def estate_tcp_session(self):
        return self._EStateCTCPSession

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
        
