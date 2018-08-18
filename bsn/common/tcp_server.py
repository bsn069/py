#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

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
    ParseIPPort = 1
    Listened = 2

class CTCPServer(tcp_accept.CTCPAccept):

    def __init__(self, loop):
        logging.info("{}".format(self))
        super().__init__(loop)

        self._EStateCTCPServer = EState.Null

    async def _parse_ip_port(self):
        logging.info("{}".format(self))
        self._CIP = CIP('0.0.0.0')
        self._CPort = CPort(10001)
        await asyncio.sleep(1)

    async def _run(self):
        logging.info("{}".format(self))
        await asyncio.sleep(10)

    async def run(self):
        logging.info("{}".format(self))
        if self._EStateCTCPServer != EState.Null:
            raise err.ErrState(self._EStateCTCPServer)

        try:
            await self._parse_ip_port()
            self._EStateCTCPServer = EState.ParseIPPort

            await self.start_listen()
            self._EStateCTCPServer = EState.Listened

            await self._run()
            logging.info("{} run end".format(self))

        except Exception as e:
            logging.error(e)

        if self._EStateCTCPServer.value > EState.Listened.value:
            await self.stop_listen()
        if self._EStateCTCPServer.value > EState.ParseIPPort.value:
            self._CIP = None
            self._CPort = None

        self._EStateCTCPServer = EState.Null

    @property
    def estate_tcp_server(self):
        return self._EStateCTCPServer

file_import_tree.file_end(__name__)
