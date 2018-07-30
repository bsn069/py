#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
import asyncio
from bsn.agent_proxy.agent_proxy import CAgentProxy

logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')

async def imp(loop):
    logging.info("{}".format(loop))

    agent_proxy = CAgentProxy()
    await agent_proxy.run()

    await asyncio.sleep(2)
    loop.stop()

def main():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(imp(loop))
    loop.run_forever()
