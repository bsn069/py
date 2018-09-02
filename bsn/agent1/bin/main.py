#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import logging
# logging.basicConfig(level = logging.INFO, format = 'bb %(asctime)s %(levelname)s %(pathname)s:%(lineno)d(%(funcName)s) %(message)s')
logging.basicConfig(level = logging.INFO, format = '%(message)s \n\t %(levelname)s  %(pathname)s:%(lineno)d(%(funcName)s)' )

from bsn.common import file_import_tree
from bsn.common import asyncio_app

from bsn.agent.agent import state_owner

class CApp(object):

    def __init__(self, loop):
        logging.info("{}".format(self))
        self._loop = loop
        self._app = state_owner.CStateOwner(self)

    @property
    def loop(self):
        return self._loop

    async def run(self):
        file_import_tree.file_print()
        logging.info("{}".format(self))
        self._app.to_state('init')

        while True:
            await asyncio.sleep(1)

def create_app(loop):
    return CApp(loop)

if __name__ == '__main__':
    asyncio_app.main(create_app, 60000)