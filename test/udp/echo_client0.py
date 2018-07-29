#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""UDP 
"""


import asyncio
import logging

class EchoClientProtocol(asyncio.DatagramProtocol):
    """EchoClientProtocol"""
    def __init__(self, msg):
        logging.info("{}".format(msg))
        super().__init__()
        self._transport = None
        self._msg = b'hello' if msg is None else msg
        self._send_count = 0

    def connection_made(self, transport):
        logging.info("on socket ready")
        self._transport = transport
        self.send_test()

    def datagram_received(self, data, addr):
        logging.info("{} {}".format(data, addr))
        # self._transport.close()
        self.send_test()

    def connection_lost(self, exc):
        logging.info("only call on self close")

    def send_test(self):
        logging.info("{0}".format(self._send_count))
        if self._send_count == 4:
            self._transport.close()
            return
        self._send_count += 1
        self._transport.sendto(self._msg, ('127.0.0.1', 10001))
        self._transport.sendto(self._msg, ('127.0.0.1', 10002))
        self._transport.sendto(self._msg, ('127.0.0.1', 10003))
        self._transport.sendto(self._msg, ('127.0.0.1', 10004))

async def coro(msg):
    logging.info("{} ".format(msg))
    loop = asyncio.get_event_loop()
    await loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(msg), local_addr=("0.0.0.0", 0))

def start(msg=None):
    logging.info("{} ".format(msg))
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(coro(msg), loop=loop)