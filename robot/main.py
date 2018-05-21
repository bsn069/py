#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import portal


async def main1(loop):
    print("main")
    p = portal.Portal()
    await p.run()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main1(loop))
    # loop.run_forever()
