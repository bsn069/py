#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class CTree(object):
    def __init__(self):
        self._uLayer = 0
        self._list = []

    def print(self):
        listOut = []
        self.tree(listOut)
        for strOut in listOut:
            print(strOut)

    def tree(self, listOut, uIndex = 0, uPrintLayer = 0, strPrefix = ''):
        uMaxIndex = 0
        uTmp = uIndex
        while uTmp < len(self._list):
            data = self._list[uTmp]
            uLayer = data[0]
            if uLayer < uPrintLayer:
                break
            if uLayer == uPrintLayer:
                uMaxIndex = uTmp
            uTmp = uTmp + 1

        while uIndex < len(self._list):
            data = self._list[uIndex]
            uLayer = data[0]
            if uLayer < uPrintLayer:
                break

            if uLayer == uPrintLayer:
                if uIndex == uMaxIndex:
                    # listOut.append('{}└──{} uIndex={} uPrintLayer={} uMaxIndex={}'.format(strPrefix, data[1], uIndex, uPrintLayer, uMaxIndex))
                    listOut.append('{}└──{}'.format(strPrefix, data[1]))
                else:
                    listOut.append('{}├──{}'.format(strPrefix, data[1]))
                    # listOut.append('{}├──{} uIndex={} uPrintLayer={} uMaxIndex={}'.format(strPrefix, data[1], uIndex, uPrintLayer, uMaxIndex))

            if uLayer == uPrintLayer + 1:
                if uIndex > uMaxIndex:
                    uIndex = self.tree(listOut, uIndex, uPrintLayer + 1, strPrefix + '   ')
                else:
                    uIndex = self.tree(listOut, uIndex, uPrintLayer + 1, strPrefix + '│   ')

            uIndex = uIndex + 1
        return uIndex - 1

    def push(self, strLine):
        self._list.append((self._uLayer, strLine))

    def enter(self, strLine):
        self.push(strLine)
        self._uLayer = self._uLayer + 1

    def leave(self):
        self._uLayer = self._uLayer - 1


"""
.
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── accept_cb.cpython-37.pyc
│   ├── add.cpython-37.pyc
│   ├── agent.cpython-37.pyc
│   ├── agent_proxy.cpython-37.pyc
│   ├── dec.cpython-37.pyc
│   └── stream_protocol.cpython-37.pyc
├── agent.py
├── agent_proxy.py
├── bin
│   └── main.py
└── test
    ├── __pycache__
    │   └── test_99_all.cpython-37.pyc
    ├── test.py
    └── test_agent_proxy.py
"""
