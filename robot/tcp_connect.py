#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
import session


async def connect(host, port, loop):
    """
    return session.Session()
    """
    logging.info("{} {}".format(host, port))
    _reader, _writer = await asyncio.open_connection(host, port, loop=loop)
    _session = session.Session(_reader, _writer)
    return _session
