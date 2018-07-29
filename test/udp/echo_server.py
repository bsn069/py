#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""UDP 
"""


import asyncio
import logging

class EchoServerProtocol(asyncio.DatagramProtocol):
    """EchoServerProtocol"""
    def __init__(self):
        logging.info("")
        super().__init__()
        self._transport = None

    def connection_made(self, transport):
        logging.info("on bind")
        self._transport = transport

    def datagram_received(self, data, addr):
        logging.info("{} {}".format(data, addr))
        self._transport.sendto(data, addr)
        if data == b'end':
            logging.info("receive end!!!")
            self._transport.close()

    def connection_lost(self, exc):
        logging.info("only call on self close")

async def coro(address, port):
    logging.info("{} {}".format(address, port))
    loop = asyncio.get_event_loop()
    protocol = EchoServerProtocol()
    await loop.create_datagram_endpoint(
        lambda: protocol, local_addr=(address, port))

def start(address="0.0.0.0", port=8888):
    logging.info("{} {}".format(address, port))
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(coro(address, port), loop=loop)