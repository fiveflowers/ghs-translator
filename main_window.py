#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11
# @Author  : Yifer Huang
# @File    : main_window.py
# @Desc    : 主窗口程序

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

from main_window_layout import Ui_MainWindow
from translator import GoogleTrans, YouDaoTrans, BaiDuTrans
import misc


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()  # 实例化UI
        self.ui.setupUi(self)  # 给主窗口加载UI
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 窗口置顶
        self.connect_signal_and_slot()  # 绑定信号和槽
        self.mytranslator = {
            '谷歌': GoogleTrans(),
            '百度': BaiDuTrans(),
            '有道': YouDaoTrans()
        }

    def connect_signal_and_slot(self):
        self.ui.comboBox_src_lang.currentIndexChanged.connect(self.slot_translate)
        self.ui.comboBox_dest_lang.currentIndexChanged.connect(self.slot_translate)
        self.ui.comboBox_trans_api.currentIndexChanged.connect(self.slot_translate)
        self.ui.plainTextEdit_src.textChanged.connect(self.slot_translate)
        self.ui.pushButton_clear.clicked.connect(self.slot_clear)
        self.ui.pushButton_copy.clicked.connect(self.slot_copy_text)

    def slot_translate(self):
        """
        槽： 翻译服务
        相关信号： src文本框变动; src/dest语言变动; 翻译接口变动
        """
        lang_dict = {
            "自动": "auto",
            "中文": "zh-CN",
            "英文": "en",
        }
        max_len = 2000  # 单次翻译字符上限
        src_text = self.ui.plainTextEdit_src.toPlainText()  # 获取src框内文本

        if src_text == '' or len(src_text) > max_len:  # 空字符或者超过字数限制调用翻译
            return

        src_text = misc.format_text(src_text)  # 格式化文本
        src_lang = self.ui.comboBox_src_lang.currentText()[-2:]  # 获取src语言

        self.ui.plainTextEdit_src.textChanged.disconnect(self.slot_translate)
        self.ui.plainTextEdit_src.setPlainText(src_text)  # 显示格式化后的文本（去换行）
        self.ui.plainTextEdit_src.textChanged.connect(self.slot_translate)

        api_type = self.ui.comboBox_trans_api.currentText()  # 获取选用的翻译API
        dest_lang = self.ui.comboBox_dest_lang.currentText()[-2:]  # 获取dest语言
        dest_text = self.mytranslator[api_type].trans(src_text, lang_dict[src_lang], lang_dict[dest_lang])  # 翻译
        self.ui.plainTextEdit_dest.setPlainText(dest_text)  # 显示翻译后的文本

    def slot_clear(self):
        """
        槽： 清空文本框内容
        """
        self.ui.plainTextEdit_src.clear()
        self.ui.plainTextEdit_dest.clear()

    def slot_copy_text(self):
        """
        槽： 复制翻译结果到剪切板
        """
        dest_text = self.ui.plainTextEdit_dest.toPlainText()  # 获取翻译结果文本
        clipboard = QApplication.clipboard()
        clipboard.setText(str(dest_text))
