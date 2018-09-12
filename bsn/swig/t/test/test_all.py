#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import u8
from bsn.common import err
from bsn.swig.shm.py import plug

import os
f_strPlugName = __file__.split(os.path.sep)[-3]
print(f_strPlugName)
import importlib
plug = importlib.import_module('bsn.swig.{}.py.plug'.format(f_strPlugName))


class Test(unittest.TestCase):

    def setUp(self): 
        self._iShmKey = 1234567
        iShmId = plug.shm_get_id(self._iShmKey)
        if iShmId > 0:
            plug.shm_delete(iShmId)
        pass

    def tearDown(self):  
        iShmId = plug.shm_get_id(self._iShmKey)
        if iShmId > 0:
            plug.shm_delete(iShmId)
        pass

    def test_new_delete(self):
        iShmId = plug.shm_new(self._iShmKey, 1)
        self.assertGreater(iShmId, 0)
        iRet = plug.shm_delete(iShmId)
        self.assertEqual(iRet, 0)
        self.assertEqual(iRet, 10)


if __name__ == '__main__':
    unittest.main()
