#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""UDP 
"""


import asyncio
import logging

class EchoClientProtocol(asyncio.DatagramProtocol):
    """EchoClientProtocol"""
    def __init__(self, msg):
        logging.info("{} ".format(msg))
        super().__init__()
        self._transport = None
        self._msg = b'hello' if msg is None else msg

    def connection_made(self, transport):
        logging.info("on socket ready")
        self._transport = transport
        self._transport.sendto(self._msg)

    def datagram_received(self, data, addr):
        logging.info("{} {}".format(data, addr))
        self._transport.close()

    def connection_lost(self, exc):
        logging.info("only call on self close")

async def coro(address, port, msg):
    logging.info("{} {} {}".format(address, port, msg))
    loop = asyncio.get_event_loop()
    await loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(msg), remote_addr=(address, port))

def start(address="127.0.0.1", port=8888, msg=None):
    logging.info("{} {} {}".format(address, port, msg))
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(coro(address, port, msg), loop=loop)