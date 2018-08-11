#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
from bsn.common import err
 

class CHost(object):
    def __init__(self, host):
        self._host = host

    def __str__(self):
        return self._host

