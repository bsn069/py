#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
from bsn.common import err


def valid(strIP):
    if type(strIP) != str:
        return False
    return re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", strIP)



class CIP(object):
    def __init__(self, ip):
        strIP = ip
        if type(ip) == CIP:
            strIP = str(ip)
        elif type(ip) == int:
            strIP = '%d.%d.%d.%d' % ((ip >> 24) & 0xff, (ip >> 16) & 0xff, (ip >> 8) & 0xff,  (ip >> 0) & 0xff)
        elif type(ip) == str:
            pass
        else:
            return err.ErrIP()

        if not valid(strIP):
            raise err.ErrIP()

        result = re.findall(r'(\d+).(\d+).(\d+).(\d+)', strIP)
        if not result:
            raise err.ErrIP()

        self.__field = (int(result[0][0]), int(
            result[0][1]), int(result[0][2]), int(result[0][3]))
        self.__str = ip
        self.__u32 = (self.__field[0] << 24) + (self.__field[1] << 16) + (self.__field[2] << 8) + self.__field[3]

    @property
    def u32(self):
        return self.__u32

    def __str__(self):
        return self.__str

    def __getitem__(self, key):
        try:
            return self.__field[key]
        except KeyError:
            return None

    def __eq__(self, other):
        return self.u32 == other.u32
