#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import ip_port

class CAgentProxy(object):

    def __init__(self):
        self.__host = None
        self.__port = None
        self.__run = False

    def run(self):
        if self.__host is None:
            raise TypeError('not set host')
        if self.__port is None:
            raise TypeError('not set port')
        if self.__run is True:
            return True
        self.__run = True

        return True

    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, u16Port):
        if self.port is not None:
            raise 
        if not ip_port.valid(u16Port): 
            raise TypeError("port invalid")
        self.__port = u16Port


