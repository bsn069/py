#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
import asyncio

logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')

async def imp(oIApp, loop, uTestSec):
    logging.info("{}".format(loop))

    oIApp.run()
    if uTestSec is not None:
        await asyncio.sleep(uTestSec)
        oIApp.stop()

def main(create_app, uTestSec):
    '''

    '''
    logging.info("{} {}".format(create_app, uTestSec))
    loop = asyncio.get_event_loop()
    oIApp = create_app(loop)
    asyncio.ensure_future(imp(oIApp, loop, uTestSec))
    loop.run_forever()

