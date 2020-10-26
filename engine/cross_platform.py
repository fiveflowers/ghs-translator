#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25
# @Author  : Yifer Huang
# @File    : cross_platform.py
# @Desc    : some misc functions for cross platform (Linux, Windows, Mac)

# hot keys
HOT_KEY_MINIMIZED = {
    "macos": "Command+M",
    "Linux": "Ctrl+M",
    "Windows": "Ctrl+M"
}
HOT_KEY_CLOSE = {
    "macos": "Command+Q",
    "Linux": "Ctrl+Q",
    "Windows": "Ctrl+Q"
}
TEXT_SRC = {
    "macos": "### 使用说明\n"
             ">> 复制需要翻译的文档到此文本框中\n"
             ">> 软件将自动“去换行”并执行翻译\n"
             "\n"
             "### 快捷键\n"
             ">> 隐藏窗口: COMMAND + M\n"
             ">> 退出程序: COMMAND + Q\n"
             "\n"
             "### 关于程序\n"
             ">> 软件更新: http://dwz.date/cWx6\n"
             ">> 问题反馈: http://dwz.date/cWxB",
    "Linux": "### 使用说明\n"
             ">> 复制需要翻译的文档到此文本框中\n"
             ">> 软件将自动“去换行”并执行翻译\n"
             "\n"
             "### 快捷键\n"
             ">> 隐藏窗口: CTRL + M\n"
             ">> 退出程序: CTRL + Q\n"
             "\n"
             "### 关于程序\n"
             ">> 软件更新: http://dwz.date/cWx6\n"
             ">> 问题反馈: http://dwz.date/cWxB",
    "Windows": "### 使用说明\n"
               ">> 复制需要翻译的文档到此文本框中\n"
               ">> 软件将自动“去换行”并执行翻译\n"
               "\n"
               "### 快捷键\n"
               ">> 隐藏窗口: CTRL + M\n"
               ">> 退出程序: CTRL + Q\n"
               "\n"
               "### 关于程序\n"
               ">> 软件更新: http://dwz.date/cWx6\n"
               ">> 问题反馈: http://dwz.date/cWxB",
}
TEXT_DEST = {
    "macos": "### Instructions \n"
             ">> Copy text to be translated into this box \n"
             "\n"
             "### Shortcuts \n"
             ">> Minimize window: COMMAND + M \n"
             ">> Exit : COMMAND + Q \n"
             "\n"
             "### About\n"
             ">> Update: http://dwz.date/cWx6 \n"
             ">> Feedback: http://dwz.date/cWxB",
    "Linux": "### Instructions \n"
             ">> Copy text to be translated into this box \n"
             "\n"
             "### Shortcuts \n"
             ">> Minimize window: CTRL + M \n"
             ">> Exit : CTRL + Q \n"
             "\n"
             "### About\n"
             ">> Update: http://dwz.date/cWx6 \n"
             ">> Feedback: http://dwz.date/cWxB",
    "Windows": "### Instructions \n"
               ">> Copy text to be translated into this box \n"
               "\n"
               "### Shortcuts \n"
               ">> Minimize window: CTRL + M \n"
               ">> Exit : CTRL + Q \n"
               "\n"
               "### About\n"
               ">> Update: http://dwz.date/cWx6 \n"
               ">> Feedback: http://dwz.date/cWxB",
}
