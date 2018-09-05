#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]
f_strAppName = __file__.split(os.path.sep)[-3]

import asyncio
import logging
logging.basicConfig(level = logging.INFO, format = '(%(funcName)s)%(message)s \n\t %(levelname)s  %(pathname)s:%(lineno)d' )

from bsn.common import asyncio_app
from bsn.common import app_base as app
from optparse import OptionParser
from optparse import OptionGroup

def _parse_arg():
    parse = OptionParser()
    group = OptionGroup(parse, 
        'App Options',
        'app special config')

    # group.add_option('-c','--config',
    #     metavar='configDir',
    #     action='store',
    #     dest='config',
    #     type="string",
    #     default = 'default',
    #     help='config dir name')

    parse.add_option_group(group)
    return app.get_args(parse)

class CApp(app.CApp):
    def __init__(self, loop, *args):
        logging.info("{} args={}".format(self, args))
        super().__init__(loop, f_strAppName, *args)

def create_app(loop, *args):
    logging.info("args={}".format(args))
    return CApp(loop, *args)

if __name__ == '__main__':
    args = _parse_arg()
    logging.info("args={}".format(args))
    asyncio_app.main(create_app, args)