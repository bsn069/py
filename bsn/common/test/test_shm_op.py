#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import shm_op
from bsn.common import err
from bsn.swig.shm.py import plug

class Test(unittest.TestCase):

    def setUp(self): 
        self._iShmKey = 12345671
        iShmId = plug.shm_get_id(self._iShmKey)
        if iShmId > 0:
            plug.shm_delete(iShmId)
        self._u32Size = 100
        iShmId = plug.shm_new(self._iShmKey, self._u32Size)
        self._iAddr = plug.shm_attach(iShmId)

    def tearDown(self):  
        plug.shm_detach(self._iAddr)
        iShmId = plug.shm_get_id(self._iShmKey)
        if iShmId > 0:
            plug.shm_delete(iShmId)

    def test_u8(self):
        u32Step = 1
        testValues = [
            (0,0),
            (1,1),
            (127,127),
            (254,254),
            (255,255),

            (256,0),
            (257,1),

            (-1,255),
            (-2,254),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u32Step * i)
            shm_op.set_u8(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = shm_op.get_u8(iAddr)
            self.assertEqual(value, outValue)

    def test_i8(self):
        u32Step = 1
        testValues = [
            (-128,-128),
            (-1,-1),
            (0,0),
            (1,1),
            (127,127),

            (128,-128),
            (129,-127),
            
            (-129,127),
            (-130,126),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u32Step * i)
            shm_op.set_i8(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = shm_op.get_i8(iAddr)
            self.assertEqual(value, outValue)

        

if __name__ == '__main__':
    unittest.main()
