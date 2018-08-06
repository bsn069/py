#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import u16
from bsn.common import err


class CPort(object):
    MIN = u16.u16.MIN + 1
    MAX = u16.u16.MAX - 1

    def __init__(self, port):
        try:
            u16Value = u16.u16(port)
        except Exception as e:
            raise err.ErrPort(e)
            
        if u16Value.value < self.MIN:
            raise err.ErrPort()
        if u16Value.value > self.MAX:
            raise err.ErrPort()

        self.__value = u16Value

    @property
    def value(self):
        return self.__value.value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if type(other) == CPort:
            return self.value == other.value
        return self.__value == other
