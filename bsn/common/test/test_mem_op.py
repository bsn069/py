#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import mem_op
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
            mem_op.set_u8(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = mem_op.get_u8(iAddr)
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
            mem_op.set_i8(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = mem_op.get_i8(iAddr)
            self.assertEqual(value, outValue)

    def test_u16(self):
        u32Step = 2
        testValues = [
            (0,0),
            (1,1),
            (65534,65534),
            (65535,65535),

            (65536,0),
            (65537,1),

            (-1,65535),
            (-2,65534),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u32Step * i)
            mem_op.set_u16(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = mem_op.get_u16(iAddr)
            self.assertEqual(value, outValue)

    def test_i16(self):
        u32Step = 2
        testValues = [
            (-32768,-32768),
            (-1,-1),
            (0,0),
            (1,1),
            (32767,32767),

            (32768,-32768),
            (32769,-32767),
            
            (-32769,32767),
            (-32770,32766),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u32Step * i)
            mem_op.set_i16(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = mem_op.get_i16(iAddr)
            self.assertEqual(value, outValue)

    def test_u32(self):
        u32Step = 4
        testValues = [
            (0,0),
            (1,1),
            (4294967294,4294967294),
            (4294967295,4294967295),

            (4294967296,0),
            (4294967297,1),

            (-1,4294967295),
            (-2,4294967294),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u32Step * i)
            mem_op.set_u32(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = mem_op.get_u32(iAddr)
            self.assertEqual(value, outValue)

    def test_i32(self):
        u32Step = 4
        testValues = [
            (-2147483648,-2147483648),
            (-1,-1),
            (0,0),
            (1,1),
            (2147483647,2147483647),

            (2147483648,-2147483648),
            (2147483649,-2147483647),
            
            (-2147483649,2147483647),
            (-2147483650,2147483646),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u32Step * i)
            mem_op.set_i32(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u32Step * i)
            value = mem_op.get_i32(iAddr)
            self.assertEqual(value, outValue)


    def test_u64(self):
        u64Step = 8
        testValues = [
            (0,0),
            (1,1),
            (18446744073709551614,18446744073709551614),
            (18446744073709551615,18446744073709551615),

            (18446744073709551616,0),
            (18446744073709551617,1),

            (-1,18446744073709551615),
            (-2,18446744073709551614),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u64Step * i)
            mem_op.set_u64(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u64Step * i)
            value = mem_op.get_u64(iAddr)
            self.assertEqual(value, outValue)

    def test_i64(self):
        u64Step = 8
        testValues = [
            (-9223372036854775808,-9223372036854775808),
            (-1,-1),
            (0,0),
            (1,1),
            (9223372036854775807,9223372036854775807),

            (9223372036854775808,-9223372036854775808),
            (9223372036854775809,-9223372036854775807),
            
            (-9223372036854775809,9223372036854775807),
            (-9223372036854775810,9223372036854775806),
        ]

        for i in range(len(testValues)):
            inValue = testValues[i][0]
            iAddr = self._iAddr + (u64Step * i)
            mem_op.set_i64(iAddr, inValue)

        for i in range(len(testValues)):
            outValue = testValues[i][1]
            iAddr = self._iAddr + (u64Step * i)
            value = mem_op.get_i64(iAddr)
            self.assertEqual(value, outValue)

        

if __name__ == '__main__':
    unittest.main()
