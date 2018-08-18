#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

from bsn.agent_proxy.agent_proxy import CAgentProxy
from bsn.common import asyncio_app

def create_app(loop):
    return CAgentProxy(loop)

if __name__ == '__main__':
    asyncio_app.main(create_app, 5)


file_import_tree.file_end(__name__)