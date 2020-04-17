#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 下午9:27
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @File    : main_window.py


from PyQt5.QtWidgets import QMainWindow
from modules.main_window_layout import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)