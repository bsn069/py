#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import u8


class CAppId(object):

    def __init__(self):
        self.__func_id = 0
        self.__inst_id = 0
        self.__u32 = 0

    @property
    def inst_id(self):
        return self.__inst_id

    @inst_id.setter
    def inst_id(self, u8InstId):
        if u8.is_u8(u8InstId):
            self.__inst_id = u8InstId
            self.__calc_u32()
            return
        raise TypeError('must in uint8 range')

    @property
    def func_id(self):
        return self.__func_id

    @func_id.setter
    def func_id(self, u8FuncId):
        if u8.is_u8(u8FuncId):
            self.__func_id = u8FuncId
            self.__calc_u32()
            return
        raise TypeError('must in uint8 range')

    @property
    def u32(self):
        return self.__u32

    @property
    def to_string(self):
        return '%u.%u' % (self.func_id, self.inst_id)

    def __calc_u32(self):
        self.__u32 = (self.func_id << 8) + self.inst_id

    def __eq__(self, oCAppIdOther):
        return self.inst_id == oCAppIdOther.inst_id

    def __str__(self):
        return 'CAppId:%s' % (self.to_string)
