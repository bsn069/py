#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common.ip import CIP
from bsn.common.port import CPort

class CIPPortErrParamNotIPPort(Exception):
    pass
class CIPPortErrParamMustIPPort(Exception):
    pass
class CIPPortErrParamNotIP(Exception):
    pass
class CIPPortErrParamNotPort(Exception):
    pass


class CIPPort(object):
    def __init__(self, oCIP, oCPort):
        '''
        oCIP must is bsn.common.ip.CIP
        oCPort must is bsn.common.port.CPort
        '''
        if type(oCIP) != CIP and type(oCPort) != CPort:
            raise CIPPortErrParamMustIPPort()
        if type(oCIP) != CIP:
            raise CIPPortErrParamNotIP()
        if type(oCPort) != CPort:
            raise CIPPortErrParamNotPort()

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

    @property
    def string(self):
        '''
        return '0.0.0.0:2777'
        '''
        return '%s:%u' % (self.ip, self.port)
