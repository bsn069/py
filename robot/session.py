#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging




class Session(object):
    """  
    """

    def __init__(self, reader, writer):
        logging.info("{}".format(self))
        self._reader = reader
        self._writer = writer

    def close(self):
        logging.info("{}".format(self))
        if self._writer:
            self._writer.transport.close()
        self._writer = None
        self._reader = None
 
async def connect(host, port, loop):
    """
    return Session()
    """
    logging.info("{} {}".format(host, port))
    _reader, _writer = await asyncio.open_connection(host, port, loop=loop)
    _session = Session(_reader, _writer)
    return _session