#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: main_window.py
# @Function: 主窗口


from PyQt5.QtWidgets import QMainWindow

from modules.main_window_layout import Ui_MainWindow
from modules.pdf_viewer import PdfViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.pdf_viewer = PdfViewer()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 加载UI设定
        self.ui.gridLayout.addWidget(self.pdf_viewer, 0, 1, 1, 1)  # 在布局中添加 pdf viewer
        self.ui.sidebar.hide()  # 逻辑隐藏侧边栏
