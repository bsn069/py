#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging
import asyncio

# logging.basicConfig(level = logging.INFO, format = 'bb %(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')

def main(create_app, *args):
    '''

    '''
    try:
        logging.info("{} args={}".format(create_app, args))
        loop = asyncio.get_event_loop()
        oIApp = create_app(loop, *args)
        # asyncio.ensure_future(oIApp.run(), loop=loop)
        # loop.run_forever()
        loop.run_until_complete(oIApp.run())
    except KeyboardInterrupt as e:
        logging.info(e)

file_import_tree.file_end(__name__)
