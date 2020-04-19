#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: main_window.py
# @Function: 主窗口


from PyQt5.QtWidgets import QMainWindow

from modules.configure import Configure
from modules.formatting import TextFormat
from modules.main_window_layout import Ui_MainWindow
from modules.pdf_viewer import PdfViewer


class MainWindow(QMainWindow):
    MAX_CHARACTERS = 2000

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 加载 UI 设定
        self.ui.sidebar.hide()  # 逻辑隐藏侧边栏

        self.list_history_filename = []
        self.list_history_filepath = []
        self.list_files_filename = []
        self.list_files_filepath = []
        self.trans_font_size = 12  # 设置翻译区字体大小

        self.formater = TextFormat()
        self.pdf_viewer = PdfViewer()  # 实例化 pdf viewer
        self.ui.gridLayout.addWidget(self.pdf_viewer, 0, 1, 1, 1)  # 在布局中添加 pdf viewer
        self.connect_signal_and_slot()  # 一梭子绑定信号与槽
        self.update_history_from_config()  # 读取历史记录

    def connect_signal_and_slot(self):
        self.pdf_viewer.signal_mouse_release_in_pdf_viewer.connect(self.slot_get_plain_text)

    def slot_get_plain_text(self):
        """
        槽
        获取Viewer中选中的文字，并显示出来
        """
        if self.pdf_viewer.hasSelection():
            raw_text = self.pdf_viewer.selectedText()  # 获得原始文本
            plain_text = self.formater.reformat(raw_text)  # 对选中的原始文字进行格式化处理（去除换行连字符）
            if len(plain_text) < self.MAX_CHARACTERS:
                self.ui.plainTextEdit_original_text.setPlainText(plain_text)  # 并显示出来
            else:
                error_message = "警告：单次选中的文字过多，超过了%s，请重新选择翻译文本" % self.MAX_CHARACTERS
                self.ui.plainTextEdit_original_text.setPlainText(error_message)  # 报错

    def update_history_from_config(self):
        config = Configure()
        temp = config.history.items('History')
        self.list_history_filename = []  # 清空内存中的列表信息
        self.list_history_filepath = []  # 清空内存中的列表信息
        for item in temp:
            self.list_history_filename.append(item[0])
            self.list_history_filepath.append(item[1])
        self.ui.listWidget_history.clear()  # 清空侧边栏的历史记录
        self.ui.listWidget_history.addItems(self.list_history_filename)  # 在侧边栏显示出来
