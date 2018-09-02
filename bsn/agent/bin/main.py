#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]
f_strAppName = __file__.split(os.path.sep)[-3]

import asyncio
import logging
logging.basicConfig(level = logging.INFO, format = '%(message)s \n\t %(levelname)s  %(pathname)s:%(lineno)d(%(funcName)s)' )

from bsn.common import asyncio_app
from bsn.common import app_base as app

class CApp(app.CApp):

    def __init__(self, loop):
        logging.info("{}".format(self))
        super().__init__(loop, f_strAppName)

def create_app(loop):
    return CApp(loop)

if __name__ == '__main__':
    asyncio_app.main(create_app, 60000)