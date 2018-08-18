#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

from bsn.common import err

class u8(object):
    MIN = 0
    MAX = (1 << 8) - 1

    def __init__(self, value):
        u8Value = value

        try:
            if type(value) == int:
                pass
            elif type(value) == str:
                u8Value = int(value)
            else:
                u8Value = int(str(value))
        except Exception:
            raise err.ErrParamType()

        if u8Value < self.MIN:
            raise err.ErrParamTooMin()
        if u8Value > self.MAX:
            raise err.ErrParamTooMax()

        self.__value = u8Value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return str(self.value)


    def __lt__(self, other):
        if type(other) == u8:
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if type(other) == u8:
            return other < self
        return self.value > other

    def __eq__(self, other):
        if self < other:
            return False
        if self > other:
            return False
        return True

    def __le__(self, other):
        return not (self > other)

    def __ge__(self, other):
        return not (self < other)


file_import_tree.file_end(__name__)        