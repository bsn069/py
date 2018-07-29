#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import portal
import logging
import test_tcp_accept
import test_session

logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')
# logger = logging.getLogger(__name__)

async def main1(loop):
    logging.info("{}".format(loop))

    # test_tcp_accept1 = test_tcp_accept.TestTCPAccept(loop)
    # test_tcp_accept1.run()

    # test = test_session.Test(loop)
    # await test.run()

    # test_tcp_connect2 = test_tcp_connect.TestTCPConnect(loop)
    # test_tcp_connect2.run()

    _portal = portal.Portal(loop)
    await _portal.run()

    await asyncio.sleep(2)
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main1(loop))
    # loop.run_until_complete(main1(loop))
    loop.run_forever()
