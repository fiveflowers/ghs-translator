#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: ghs-translator.py
# @Function: 主程序入口


import sys

from PyQt5.QtWidgets import QApplication

from modules.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()                           # 实例化主程序
    mainWindow.show()                                   # 显示主窗口
    sys.exit(app.exec_())                               # 退出程序
