#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import asyncio
from bsn.common import ip_port
from bsn.common.ip_ip import CIP
from bsn.common.ip_port import CPort
from bsn.common import tcp_accept

class CAgentProxyErr(Exception):
    pass
class CAgentProxyErrNoListenAddr(CAgentProxyErr):
    pass
class CAgentProxyErrNoListenPort(CAgentProxyErrNoListenAddr):
    pass
class CAgentProxyErrNoListenIP(CAgentProxyErrNoListenAddr):
    pass
class CAgentProxyErrIP(CAgentProxyErr):
    pass
class CAgentProxyErrPort(CAgentProxyErr):
    pass

class CAgentProxy(object):

    def __init__(self):
        self.__ip = None
        self.__port = None
        self.__run = False

    async def run(self, loop):
        if self.ip is None and self.port is None:
            raise CAgentProxyErrNoListenAddr('not set ip port')
        if self.ip is None:
            raise CAgentProxyErrNoListenIP('not set ip')
        if self.port is None:
            raise CAgentProxyErrNoListenPort('not set port')
        if self.__run is True:
            return 
        self.__run = True
        self.__tcp_accept = tcp_accept.CTCPAccept(self, loop)
        self.__tcp_accept.listen(self.ip., self._port)

    @property
    def ip(self):
        return self.__ip

    @property
    def port(self):
        return self.__port

    @ip.setter
    def ip(self, oIP):
        if type(oIP) != CIP:
            raise CAgentProxyErrIP("must CIP")
        if self.ip is not None:
            raise CAgentProxyErrIP("had set ip")
        self.__ip = oIP

    @port.setter
    def port(self, oPort):
        if type(oPort) != CPort:
            raise CAgentProxyErrPort("must CPort")
        if self.port is not None:
            raise CAgentProxyErrPort("had set port")
        self.__port = oPort



