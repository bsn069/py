#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import asyncio

async def main1(loop):
    print("main")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main1(loop))
    # loop.run_forever()