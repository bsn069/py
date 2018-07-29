#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# from .app_id import *


class CAppIPC(object):

    def __init__(self, oCAppId):
        self.__oCAppId = oCAppId

    def send(self, oCAppId, pbyBuff, u32Size):
        return True

    @property
    def app_id(self):
        return self.__oCAppId
