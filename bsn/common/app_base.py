#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]
f_strAppName = __file__.split(os.path.sep)[-3]

import logging
import importlib
import asyncio

class CApp(object):

    def __init__(self, loop, strAppName):
        logging.info("{} strAppName={}".format(self, strAppName))
        self._loop = loop
        self._strAppName = strAppName

        strAppPackagePath = 'bsn.{}.main.state_owner'.format(strAppName)
        state_owner = importlib.import_module(strAppPackagePath)

        self._mapConfig = None
        self._load_config('default')

        self._main = state_owner.CStateOwner(self, self, 0)

    @property
    def loop(self):
        return self._loop

    @property
    def map_config(self):
        return self._mapConfig

    @property
    def main(self):
        return self._main

    @property
    def app_name(self):
        return self._strAppName

    def config(self, key):
        return self.map_config[key]

    def _load_config(self, strConfigName):
        strConfigPackageFullName = 'bsn.{}.conifg.{}.config'.format(self.app_name, strConfigName)
        mConfig = importlib.import_module(strConfigPackageFullName)
        self._mapConfig = mConfig.f_mapConfig

    async def run(self):
        file_import_tree.file_print()
        logging.info("{}".format(self))
        self._main.to_state('init')

        while True:
            await asyncio.sleep(1)

file_import_tree.file_end(__name__)