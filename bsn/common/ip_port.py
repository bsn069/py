#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common.ip import CIP
from bsn.common.port import CPort

class CIPPortErrNotCIP(Exception):
    pass
class CIPPortErrNotCPort(Exception):
    pass

class CIPPort(object):
    def __init__(self, oCIP, oCPort):
        '''
        oCIP must is bsn.common.ip.CIP
        oCPort must is bsn.common.port.CPort
        '''
        if type(oCIP) != CIP:
            raise CIPPortErrNotCIP()
        if type(oCPort) != CPort:
            raise CIPPortErrNotCPort()

        self.__ip = oCIP
        self.__port = oCPort

    @property
    def ip(self):
        '''
        return bsn.common.ip.CIP
        '''
        return self.__ip

    @property
    def port(self):
        '''
        return bsn.common.port.CPort
        '''
        return self.__port
