#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
import asyncio

logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')

def main(create_app, uTestSec):
    '''

    '''
    try:
        logging.info("{} {}".format(create_app, uTestSec))
        loop = asyncio.get_event_loop()
        oIApp = create_app(loop)
        # asyncio.ensure_future(oIApp.run(), loop=loop)
        # loop.run_forever()
        loop.run_until_complete(oIApp.run())
    except KeyboardInterrupt as e:
        logging.info(e)


