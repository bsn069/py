#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.agent_proxy import agent_proxy
from bsn.common.ip_ip import CIP
from bsn.common.ip_port import CPort

class Test(unittest.TestCase):

    def setUp(self): 
        self.__agent_proxy = agent_proxy.CAgentProxy()
        pass

    def tearDown(self):  
        pass
        
    def test_2_(self):
        self.__agent_proxy.ip = CIP('0.0.0.0')
        self.__agent_proxy.port = CPort(10000)

    def test_2_err_run(self):
        with self.assertRaises(agent_proxy.CAgentProxyErrNoListenAddr):
            self.__agent_proxy.run()


    def test_2_err_ip(self):
        with self.assertRaises(agent_proxy.CAgentProxyErrIP):
            self.__agent_proxy.ip = '0.0.0.0'
        self.__agent_proxy.ip = CIP('0.0.0.0')
        with self.assertRaises(agent_proxy.CAgentProxyErrIP):
            self.__agent_proxy.ip = CIP('0.0.0.0')

    def test_2_err_port(self):
        with self.assertRaises(agent_proxy.CAgentProxyErrPort):
            self.__agent_proxy.port = 3433
        self.__agent_proxy.port = CPort(10000)
        with self.assertRaises(agent_proxy.CAgentProxyErrPort):
            self.__agent_proxy.port = CPort(22222)

    def test_2_no_port(self):
        self.__agent_proxy.ip = CIP('0.0.0.0')
        with self.assertRaises(agent_proxy.CAgentProxyErrNoListenPort):
            self.__agent_proxy.run()

    def test_2_no_ip(self):
        self.__agent_proxy.port = CPort(10000)
        with self.assertRaises(agent_proxy.CAgentProxyErrNoListenIP):
            self.__agent_proxy.run()
        
if __name__ == '__main__':
    unittest.main()
