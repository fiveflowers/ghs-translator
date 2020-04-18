#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: cross_platform.py
# @Function: 增加跨平台/多系统支持


import platform


class CrossPlatform(object):
    @staticmethod
    def path_converter(path):
        """
        把文件路径转换成当前系统的格式
        :param path: 文件路径
        :return: 匹配当前系统的文件路径
        """
        system_str = platform.system()
        if system_str == 'Windows':
            return str(path).replace(r'\\', r'/')
        else:  # Linux 或者 Mac Os
            return path
