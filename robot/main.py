#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import portal
import logging

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

async def main1(loop):
    logging.info("main1")
    p = portal.Portal()
    await p.run()
    await asyncio.sleep(5)
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main1(loop))
    # loop.run_until_complete(main1(loop))
    loop.run_forever()
