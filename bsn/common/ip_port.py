#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def min():
    return 1


def max():
    return 65535


def valid(u16Port):
    if type(u16Port) != int:
        return False
    if u16Port < min():
        return False
    if u16Port > max():
        return False
    return True


class CIPPortErr(Exception):
    pass


class CPort(object):
    def __init__(self, u16Port):
        if not valid(u16Port):
            raise CIPPortErr()
        self.__value = u16Port

    @property
    def value(self):
        return self.__value
