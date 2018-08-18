#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')

from bsn.common import asyncio_app
from bsn.agent.agent import CAgent

def create_app(loop):
    return CAgent(loop)

if __name__ == '__main__':
    asyncio_app.main(create_app, 60)