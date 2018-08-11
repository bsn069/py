#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import asyncio
from bsn.common.ip_port import CIPPort
from bsn.common.ip import CIP
from bsn.common.port import CPort
from bsn.common import err
import logging
import enum
from bsn.common import tcp_accept

class EState(enum.Enum):
    Null = 0
    WaitRun = 1
    Runing = 2
    WaitClose = 3

class CTCPServer(tcp_accept.CTCPAcceptCB):

    def __init__(self, loop):
        logging.info("{}".format(self))

        self._EState = EState.Null
        self._CTCPAccept = None

        self._CIP = None
        self._CPort = None

        self._loop = loop

    def _parse_arg(self):
        logging.info("{}".format(self))

        # self._CIP = CIP('0.0.0.0')
        # self._CPort = CPort(10001)

    def run(self):
        logging.info("{}".format(self))
        if self._EState != EState.Null:
            raise err.ErrState(self._EState)
            
        try:
            self._parse_arg()
        except Exception as e:
            raise err.ErrArg(e)

        self._EState = EState.WaitRun
        asyncio.ensure_future(self._run(), loop=self._loop)

    def stop(self):
        logging.info("{}".format(self))
        if self._EState != EState.Runing:
            raise err.ErrState(self._EState)
            
        self._EState = EState.WaitClose
        asyncio.ensure_future(self._stop(), loop=self._loop)

    async def _run(self):
        logging.info("{}".format(self))
        self._CTCPAccept = tcp_accept.CTCPAccept(self._loop, self)
        self._CTCPAccept.start_listen(self._CIP, self._CPort)

    async def _stop(self):
        self._CTCPAccept.stop_listen()
        self._CTCPAccept = None

    @property
    def ip(self):
        return self._CIP

    @property
    def port(self):
        return self._CPort

    def _on_tcp_start_listen(self):
        logging.info("{}".format(self))
        if self._EState != EState.WaitRun:
            raise err.ErrState(self._EState)
        self._EState = EState.Runing

    def _on_tcp_stop_listen(self):
        logging.info("{}".format(self))
        if self._EState != EState.WaitClose:
            raise err.ErrState(self._EState)

        self._CTCPAccept = None
        self._EState = EState.Null
        self._loop.stop()

