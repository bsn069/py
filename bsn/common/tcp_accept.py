#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

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
    WaitClose = 3
    Closeing = 4
    Listening = 5


class CTCPAcceptCB(object):
    '''
    '''
    def __init__(self):
        logging.info("{}".format(self))

    def _create_session(self):
        '''
        tcp_session.CTCPSession()
        '''
        logging.info("{}".format(self))
        return tcp_session.CTCPSession()

    def _on_tcp_start_listen(self):
        logging.info("{}".format(self))

    def _on_tcp_stop_listen(self):
        logging.info("{}".format(self))



class CTCPAccept(object):
    """  
    """

    def __init__(self, loop, oCTCPAcceptCB):
        """
        accept_cb ITCPAcceptCB
        """
        logging.info("{}".format(self))
        self._loop = loop
        self._ip = None
        self._port = None
        self._state = EState.Null
        self._server = None
        self._oCTCPAcceptCB = oCTCPAcceptCB

    def start_listen(self, ip, port):
        '''
        ip CIP
        port CPort
        '''
        logging.info("{}".format(self))
        if type(ip) != CIP:
            raise err.ErrIP(ip)
        if type(port) != CPort:
            raise err.ErrPort(port)
        if self._state is not EState.Null:
            raise err.ErrState(self._state)

        self._ip = ip
        self._port = port
        self._state = EState.WaitListen
        asyncio.ensure_future(self._start_listen_async(), loop=self._loop)

    def stop_listen(self):
        logging.info("{}".format(self))
        if self._state is not EState.Listened:
            raise err.ErrState(self._state)

        self._state = EState.WaitClose
        asyncio.ensure_future(self._stop_listen_async(), loop=self._loop)

    async def _stop_listen_async(self):
        logging.info("{}".format(self))
        if self._state is not EState.WaitClose:
            return 

        self._state = EState.Closeing
        self._server.close()
        await self._server.wait_closed()
        self._server = None
        self._state = EState.Null
        self._oCTCPAcceptCB._on_tcp_stop_listen()

    async def _start_listen_async(self):
        logging.info("{}".format(self))
        if self._state is not EState.WaitListen:
            return 

        def factory():
            return self._oCTCPAcceptCB._create_tcp_session()

        self._state = EState.Listening
        self._server = await self._loop.create_server(
            factory, str(self._ip), self._port.value)
        self._state = EState.Listened
        self._oCTCPAcceptCB._on_tcp_start_listen()
