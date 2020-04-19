#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: formatting.py
# @Function: 格式化字符串


import os
import re


class TextFormat:
    def __init__(self):
        self.en_dict = []  # 初始化英语单词词典
        self.load_dict()

    def load_dict(self):
        path = os.path.join(os.getcwd(), "resource", "dict", "words_alpha.txt")
        with open(path, 'r') as f:
            for line in f:
                self.en_dict.append(line.strip('\n'))
        print("字典导入成功...")

    def reformat(self, raw_text):
        plain_text = ''  # 返回的结果
        words = str(raw_text).split()
        for word in words:
            if '-' in word:
                word_without_dash = word.replace('-', '')
                word_en = re.split(r" |\.|,|!|\?|\)|\(|\[|\]", word_without_dash)[0]  # 正则表达式，处理那些句尾带有符号的单词
                if word_en in self.en_dict:  # 很好理解，一般复合词，连字符两边都是正常词汇的词
                    plain_text = plain_text + word_without_dash + ' '  # 处理了连字符只是用于换行的情况
                else:
                    plain_text = plain_text + word + ' '  # 说明这个连字符不能去掉，是用来构成单词的
            else:
                plain_text = plain_text + word + ' '
        print("字符串格式化成功...")
        return plain_text
