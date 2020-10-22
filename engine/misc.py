#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13
# @Author  : Yifer Huang
# @File    : misc.py
# @Desc    : 杂项函数


def format_text(text):
    """
    格式化字符串, 主要用于处理 PDF 复制的换行
    :param text: 输入的原始文本
    :return: 格式化后的文本
    """
    text = text.replace('\n', " ")
    return text
