#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11
# @Author  : Yifer Huang
# @File    : main.py
# @Desc    : 主程序

import sys

from PyQt5.QtWidgets import QApplication

from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()  # 实例化主程序
    mainWindow.show()  # 显示主窗口
    sys.exit(app.exec_())  # 退出程序
