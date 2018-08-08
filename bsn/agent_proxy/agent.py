#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.app_ipc.app_id import CAppId
from bsn.common import u8
from bsn.agent_proxy import stream_protocol

class CAgent(object):
    '''
    '''

    def __init__(self, oCStreamProtocol):
        self._oCStreamProtocal = oCStreamProtocol

    def init(self):
        return True



