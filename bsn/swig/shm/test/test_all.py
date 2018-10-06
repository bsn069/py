#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import u8
from bsn.common import err
# from bsn.swig.shm.py import plug
from ctypes import * 

import os
f_strPlugName = __file__.split(os.path.sep)[-3]
print(f_strPlugName)
import importlib
plug = importlib.import_module('bsn.swig.{}.py.plug'.format(f_strPlugName))


class Test(unittest.TestCase):

    def setUp(self): 
        self._iShmKey = 12345671
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
        u32Size = 10
        iShmId = plug.shm_new(self._iShmKey, u32Size)
        self.assertGreater(iShmId, 0)

        iShmIdGet = plug.shm_get_id(self._iShmKey)
        self.assertEqual(iShmIdGet, iShmId)

        iSize = plug.shm_size(iShmId)
        self.assertEqual(iSize, u32Size)

        iAddr = plug.shm_attach(iShmId)
        print(iAddr)
        pvAddr = cast(iAddr, POINTER(c_int))
        pvAddr.contents.value = 0x01020304
        print(pvAddr.contents)

        pcTmp = cast(iAddr, POINTER(c_int))
        print(pcTmp.contents)

        iRet = plug.shm_detach(iAddr)
        self.assertEqual(iRet, 0)

        iAddr = plug.shm_attach(iShmId)
        print('u8',iAddr)
        pvAddr = cast(iAddr+3, POINTER(c_uint8))
        print('u8', pvAddr.contents)
        print('u8', pvAddr.contents.value)
        iRet = plug.shm_detach(iAddr)
        self.assertEqual(iRet, 0)

        iRet = plug.shm_delete(iShmId)
        self.assertEqual(iRet, 0)

if __name__ == '__main__':
    unittest.main()
