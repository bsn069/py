#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import asyncio
import logging
logging.basicConfig(level = logging.INFO, format = '%(message)s \n\t %(levelname)s  %(pathname)s:%(lineno)d(%(funcName)s)' )

from bsn.common import file_import_tree
from bsn.common import asyncio_app

from bsn.template_app.main import state_owner

class CApp(object):

    def __init__(self, loop):
        logging.info("{}".format(self))
        self._loop = loop
        self._main = state_owner.CStateOwner(self)

    @property
    def loop(self):
        return self._loop

    async def run(self):
        file_import_tree.file_print()
        logging.info("{}".format(self))
        self._main.to_state('init')

        while True:
            await asyncio.sleep(1)

def create_app(loop):
    return CApp(loop)

if __name__ == '__main__':
    asyncio_app.main(create_app, 60000)