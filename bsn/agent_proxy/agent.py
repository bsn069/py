#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.app_ipc.app_id import CAppId
from bsn.common import u8

class CAgent(object):

    def __init__(self):
        self.__app_id = CAppId()

    def init(self):
        return True



