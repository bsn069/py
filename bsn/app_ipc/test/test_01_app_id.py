#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest

from bsn.app_ipc.app_id import CAppId
from bsn.common import u8


class Test(unittest.TestCase):

    def setUp(self): 
        self.__app_id = CAppId()

    def tearDown(self):  
        pass
        
    def test_01_default(self):
        self.assertEqual(self.__app_id.func_id, 2)
        self.assertEqual(self.__app_id.inst_id, 0)
        self.assertEqual(self.__app_id.u32, 0)
        self.assertEqual(self.__app_id.to_string, '0.0')
        self.assertEqual(str(self.__app_id), 'CAppId:0.0')

    def test_01_set_inst(self):
        self.__app_id.inst_id = 1
        self.assertEqual(self.__app_id.func_id, 0)
        self.assertEqual(self.__app_id.inst_id, 1)
        self.assertEqual(self.__app_id.u32, 1)
        self.assertEqual(self.__app_id.to_string, '0.1')
        self.assertEqual(str(self.__app_id), 'CAppId:0.1')

        with self.assertRaises(TypeError):
            self.__app_id.inst_id = '1'
        self.assertEqual(self.__app_id.inst_id, 1)

        with self.assertRaises(TypeError):
            self.__app_id.inst_id = u8.u8_min() -1
        self.assertEqual(self.__app_id.inst_id, 1)

        with self.assertRaises(TypeError):
            self.__app_id.inst_id = u8.u8_max() + 1
        self.assertEqual(self.__app_id.inst_id, 1)

        self.__app_id.inst_id = 255
        self.assertEqual(self.__app_id.func_id, 0)
        self.assertEqual(self.__app_id.inst_id, 255)
        self.assertEqual(self.__app_id.u32, 255)
        self.assertEqual(self.__app_id.to_string, '0.255')
        self.assertEqual(str(self.__app_id), 'CAppId:0.255')


    def test_01_set_func(self):
        self.__app_id.func_id = 1
        self.assertEqual(self.__app_id.func_id, 1)
        self.assertEqual(self.__app_id.inst_id, 0)
        self.assertEqual(self.__app_id.u32, 256)
        self.assertEqual(self.__app_id.to_string, '1.0')
        self.assertEqual(str(self.__app_id), 'CAppId:1.0')

        with self.assertRaises(TypeError):
            self.__app_id.func_id = '1'
        self.assertEqual(self.__app_id.func_id, 1)

        with self.assertRaises(TypeError):
            self.__app_id.func_id = u8.u8_min() -1
        self.assertEqual(self.__app_id.func_id, 1)

        with self.assertRaises(TypeError):
            self.__app_id.func_id = u8.u8_max() + 1
        self.assertEqual(self.__app_id.func_id, 1)

        self.__app_id.func_id = 255
        self.assertEqual(self.__app_id.func_id, 255)
        self.assertEqual(self.__app_id.inst_id, 0)
        self.assertEqual(self.__app_id.u32, 255 << 8)
        self.assertEqual(self.__app_id.to_string, '255.0')
        self.assertEqual(str(self.__app_id), 'CAppId:255.0')

    def test_01_set_func_inst(self):
        self.__app_id.func_id = 1
        self.__app_id.inst_id = 1
        self.assertEqual(self.__app_id.func_id, 1)
        self.assertEqual(self.__app_id.inst_id, 1)
        self.assertEqual(self.__app_id.u32, (1 << 8) + 1)
        self.assertEqual(self.__app_id.to_string, '1.1')
        self.assertEqual(str(self.__app_id), 'CAppId:1.1')


if __name__ == '__main__':
    unittest.main()
