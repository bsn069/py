#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
from bsn.common.ip_port import CIPPort
from bsn.common.ip import CIP
from bsn.common.port import CPort
from bsn.common import tcp_accept
from bsn.common import err
from bsn.common import tcp_server
import logging
from bsn.agent.agent_proxy import agent_proxy

from bsn.pb import comm_pb2

class CAgent(object):

    def __init__(self, loop):
        logging.info("{}".format(self))

    async def _run(self):
        file_import_tree.file_print()
        logging.info("{}".format(self))

        

file_import_tree.file_end(__name__)
