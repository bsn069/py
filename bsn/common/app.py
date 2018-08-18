#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

class CApp(object):

    def __init__(self):
        logging.info("{}".format(self))

    def run(self):
        logging.info("{}".format(self))

    def stop(self):
        logging.info("{}".format(self))
    
file_import_tree.file_end(__name__)