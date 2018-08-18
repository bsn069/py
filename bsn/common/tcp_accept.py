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
from bsn.common import tcp_session


class EState(enum.Enum):
    Null = 0
    WaitListen = 1
    Listened = 2


class CTCPAccept(object):
    """  
    """

    def __init__(self, loop):
        """
        """
        logging.info("{}".format(self))
        self._EStateTCPAccept = EState.Null
        self._ServerTCPAccept = None

        self._CIP = None
        self._CPort = None

        self._loop = loop

    def _create_session(self):
        '''
        return asyncio.protocols.Protocol
        '''
        return None

    async def start_listen(self):
        '''
        '''
        logging.info("{} {} {}".format(self, self._CIP, self._CPort))

        if type(self._CIP) != CIP:
            raise err.ErrIP(self._CIP)
        if type(self._CPort) != CPort:
            raise err.ErrPort(self._CPort)
        if self._EStateTCPAccept != EState.Null:
            raise err.ErrState(self._EStateTCPAccept)

        try:
            self._ServerTCPAccept = await self._loop.create_server(
                self._create_session, str(self._CIP), self._CPort.value)
        except OSError as e:
            logging.error(e)
            raise err.ErrListenFail(e) 

        self._EStateTCPAccept = EState.Listened

    async def stop_listen(self):
        logging.info("{}".format(self))
        if self._EStateTCPAccept != EState.Listened:
            raise err.ErrState(self._EStateTCPAccept)

        self._ServerTCPAccept.close()
        await self._ServerTCPAccept.wait_closed()
        self._ServerTCPAccept = None
        self._EStateTCPAccept = EState.Null

    @property
    def estate_tcp_accept(self):
        return self._EStateTCPAccept

    @property
    def ip(self):
        return self._CIP

    @property
    def port(self):
        return self._CPort


file_import_tree.file_end(__name__)