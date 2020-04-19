#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: configure.py
# @Function: 配置文件的存取


import configparser
import os


class Configure(object):
    def __init__(self):
        super(Configure, self).__init__()
        self.path_history = os.path.join(os.getcwd(), 'conf', 'history.ini')
        self.history = configparser.ConfigParser()
        self.history.read(self.path_history)

    def add_history(self, key, value):
        with open(self.path_history, 'w') as f:
            self.history.set('History', key, value)
            self.history.write(f)
