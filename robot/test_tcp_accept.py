#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import tcp_accept
 


class TestTCPAccept(tcp_accept.TCPAcceptCB):

    def __init__(self, loop):
        super().__init__()
        self._host = "localhost"
        self._port = 9262
        self._tcp_accept = tcp_accept.TCPAccept(self, loop)

    def run(self):
        self._tcp_accept.listen(self._host, self._port)
 

