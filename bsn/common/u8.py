#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def u8_min():
    return 0

def u8_max():
    return 255

def is_u8(u8):
    if type(u8) != int:
        return False
    if u8 < u8_min():
        return False
    if u8 > u8_max():
        return False
    return True