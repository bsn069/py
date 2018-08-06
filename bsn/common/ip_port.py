#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common.ip import CIP
from bsn.common.port import CPort
from bsn.common import err

class CIPPort(object):
    def __init__(self, ip, port):
        '''
        '''

        try:
            oCIP = CIP(ip)
        except Exception:
            raise err.ErrParamNotIP()

        try:
            oCPort = CPort(port)
        except Exception:
            raise err.ErrParamNotPort()

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
