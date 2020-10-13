#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11
# @Author  : Yifer Huang
# @File    : translator.py
# @Desc    : 翻译服务API

from googletrans import Translator


class GoogleTrans(Translator):
    def __init__(self):
        super(GoogleTrans, self).__init__(service_urls=['translate.google.cn'])  # 修改为中国源

    def trans(self, text, src_lang='auto', dest_lang='zh-cn'):
        """
        标准化翻译接口

        Args:
            text: 待翻译的文本
            src_lang: 源语言
            dest_lang: 目的语言

        Returns: 翻译好的文本

        """
        return super(GoogleTrans, self).translate(text=text, dest=dest_lang, src=src_lang).text


class YouDaoTrans:
    def __init__(self):
        pass

    def trans(self, text, src_lang='auto', dest_lang='zh-cn'):
        """
        标准化翻译接口

        Args:
            text: 待翻译的文本
            src_lang: 源语言
            dest_lang: 目的语言

        Returns: 翻译好的文本

        """
        return "有道翻译服务即将上线..."


class BaiDuTrans:
    def __init__(self):
        pass

    def trans(self, text, src_lang='auto', dest_lang='zh-cn'):
        """
        标准化翻译接口

        Args:
            text: 待翻译的文本
            src_lang: 源语言
            dest_lang: 目的语言

        Returns: 翻译好的文本

        """
        return "百度翻译服务即将上线..."
