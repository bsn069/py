#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re


def min():
    return 1


def max():
    return 65535


def valid(strIP):
    if type(strIP) != str:
        return False
    return re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", strIP)


class CIPErr(Exception):
    pass


class CIP(object):
    def __init__(self, strIP):
        if not valid(strIP):
            raise CIPErr()

        result = re.findall(r'(\d+).(\d+).(\d+).(\d+)', strIP)
        if not result:
            raise CIPErr()

        self.__field = (int(result[0][0]), int(
            result[0][1]), int(result[0][2]), int(result[0][3]))
        self.__str = strIP
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
