#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import tree
from bsn.common import err


class Test(unittest.TestCase):

    def setUp(self): 
        self._tree = tree.CTree()
        print('---------------------')

    def tearDown(self):  
        self._tree.print()

    def test_1_(self):
        self._tree.enter("A")
        self._tree.leave()

    def test_2_(self):
        self._tree.enter("A")
        self._tree.leave()
        self._tree.enter("A")
        self._tree.leave()

    def test_3_(self):
        self._tree.push("A1")
        self._tree.push("A2")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.push("B2")
        self._tree.leave()
        self._tree.push("B2")
        self._tree.leave()
        self._tree.push("B2")
        self._tree.push("B2")
        self._tree.leave()
        self._tree.push("A4")
        self._tree.push("A5")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.enter("A3")
        self._tree.push("B1")
        self._tree.push("B2")
        self._tree.leave()
        self._tree.push("B2")
        self._tree.leave()
        self._tree.push("B2")
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()
        self._tree.leave()



if __name__ == '__main__':
    unittest.main()
