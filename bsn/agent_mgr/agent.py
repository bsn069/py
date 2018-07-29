#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class CAgent(object):

    def __init__(self, strHost, u16Port):
        self.__host = None
        self.__port = None

    def init(self):
        return True

    def uninit(self):
        return True

