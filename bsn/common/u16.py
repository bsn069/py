#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from bsn.common import err

class u16(object):
    MIN = 0
    MAX = (1 << 16) - 1

    def __init__(self, value):
        u16Value = value

        try:
            if type(value) == int:
                pass
            elif type(value) == str:
                u16Value = int(value)
            else:
                u16Value = int(str(value))
        except Exception:
            raise err.ErrParamType()

        if u16Value < self.MIN:
            raise err.ErrParamTooMin()
        if u16Value > self.MAX:
            raise err.ErrParamTooMax()

        self.__value = u16Value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if type(other) == u16:
            return self.value == other.value
        return False