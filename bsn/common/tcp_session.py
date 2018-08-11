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
        self._uPkgLengthBit = 2 # pkg length value use bit
        self._uPkgLengthMax = 10 # pkg length value max
        self._uWaitLength = 2
        self._bLength = True
        self._uRecvByte = 0
        self._uSendByte = 0
        self._uRecvPkg = 0
        self._uSendPkg = 0

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
        logging.info("{} type(data):{} {} len(data):{}".format(self, type(data), data, len(data)))
        uDataLength = len(data)
        self._uRecvByte = self._uRecvByte + uDataLength
        uProcBegin = 0
        uLeftDataLength = uDataLength

        try:
            while uLeftDataLength > 0:
                uWaitLength = self._uWaitLength
                if uLeftDataLength < uWaitLength:
                    self._uWaitLength = uWaitLength - uLeftDataLength
                    self._parse_pkg(data[uProcBegin:uProcBegin+uLeftDataLength])
                    break

                uProcEnd = uProcBegin + uWaitLength
                self._uWaitLength = 0
                self._parse_pkg(data[uProcBegin:uProcEnd])
                uProcBegin = uProcEnd
                uLeftDataLength = uDataLength - uProcBegin
        except err.ErrPkgLength as e:
            logging.error(e)
            self.close()

    def _parse_pkg(self, data):
        logging.info("{} self._bLength:{} self._uWaitLength:{} {} ".format(self, self._bLength, self._uWaitLength, data))

        self._read_buff.extend(data)
        if self._uWaitLength == 0:
            byData = bytes(self._read_buff)
            self._read_buff.clear()
            if self._bLength:
                uWaitLength = int.from_bytes(byData, 'little')
                if uWaitLength > self._uPkgLengthMax:
                    logging.error("uWaitLength:{}".format(uWaitLength))
                    raise err.ErrPkgLength()
                self._uWaitLength = uWaitLength
                logging.info('self._uWaitLength:{}'.format(self._uWaitLength))
            else:
                self._uWaitLength = self._uPkgLengthBit
                self._on_recv_pkg(byData)
            self._bLength = not self._bLength

    def _on_recv_pkg(self, byData):
        logging.info("{} byData:{}".format(self, byData))
        self._uRecvPkg = self._uRecvPkg + 1

    def eof_received(self):
        logging.info("{}".format(self))


    def flush(self):
        self._uSendByte = self._uSendByte + len(self._write_buff)
        self._transport.write(self._write_buff)

    def close(self):
        return self._transport.close()

    def send(self, data):
        logging.info("{} {}".format(self, data))
        self._write_buff.extend(data)
        
    def send_pkg(self, data):
        length = len(data)
        byLength = length.to_bytes(2, byteorder='little')
        self._uSendPkg = self._uSendPkg + 1

        self.send(byLength)
        self.send(data)
