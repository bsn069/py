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
from bsn.common import msg_send_pkg
from bsn.common import msg_recv_pkg

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
        logging.info("1{}".format(self))
        self._CMsgSendPkg = msg_send_pkg.CMsgSendPkg(self.send)
        logging.info("2{}".format(self))
        self._CMsgRecvPkg = msg_recv_pkg.CMsgRecvPkg(self.on_recv_msg)
        logging.info("3{}".format(self))

        self._transport = None
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
        logging.info("{} type(data):{} len(data):{}".format(self, type(data), len(data)))
        self._CMsgRecvPkg.proc_data(data)

    def on_recv_msg(self, oCMsg):
        '''
        oCMsg msg.CMsg
        '''
        pass

    def eof_received(self):
        logging.info("{}".format(self))

    def flush(self):
        self._transport.write(self._write_buff)

    def close(self):
        return self._transport.close()

    def send(self, data):
        logging.info("{} {}".format(self, data))
        self._write_buff.extend(data)
        
    def send_pkg(self, cmd, data):
        logging.info("{} cmd={}".format(self, cmd))
        self._CMsgSendPkg.send_pkg(cmd, data)

file_import_tree.file_end(__name__)        
