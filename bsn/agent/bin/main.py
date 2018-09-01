#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import logging

from bsn.common import file_import_tree
from bsn.common import asyncio_app

from bsn.agent.agent import state_owner
from bsn.agent.agent import state_enum

class CApp(object):

    def __init__(self, loop):
        logging.info("{}".format(self))
        self._loop = loop
        self._app = state_owner.CStateOwner(self)

    @property
    def loop(self):
        return self._loop

    async def run(self):
        logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')
        file_import_tree.file_print()
        logging.info("{}".format(self))
        self._app.to_state(state_enum.EState.Init)

        while True:
            await asyncio.sleep(1)

def create_app(loop):
    return CApp(loop)

if __name__ == '__main__':
    asyncio_app.main(create_app, 60000)