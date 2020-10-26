#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11
# @Author  : Yifer Huang
# @File    : main_window.py
# @Desc    : 主窗口程序

import platform
import threading
import time

from PyQt5 import QtCore
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QSystemTrayIcon

from engine import misc
from engine.cross_platform import HOT_KEY_MINIMIZED, HOT_KEY_CLOSE, TEXT_SRC, TEXT_DEST
from engine.translator import GoogleTrans, BaiDuTrans
from main_window_layout import Ui_MainWindow


class MainWindow(QMainWindow):
    signal_thread = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.platform = platform.system()  # 获取当前系统
        self.ui = Ui_MainWindow()  # 实例化UI
        self.ui.setupUi(self)  # 给主窗口加载UI

        # 界面的一些初始化操作
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 窗口置顶
        self.connect_signal_and_slot()  # 绑定信号和槽
        self.init_customized_ui()

        # 一些全局变量
        self.FLAG = False  # 翻译服务 全局 Flag
        self.last_trans_time = time.time()  # 存储上次翻译的时间戳

        # 子线程
        self.trans_thread = threading.Thread(target=self.action)  # 新建子线程
        self.trans_thread.setDaemon(True)  # 守护进程
        self.trans_thread.start()  # 启动线程

        # 翻译器API
        self.mytranslator = {
            '谷歌': GoogleTrans(),
            '百度': BaiDuTrans(),
        }

        # 快捷键
        QShortcut(QKeySequence(self.tr(HOT_KEY_MINIMIZED[self.platform])), self, self.showMinimized)  # 最小化
        QShortcut(QKeySequence(self.tr(HOT_KEY_CLOSE[self.platform])), self, self.close)  # 关闭程序

        # 托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('images/translate_tray.png'))
        self.tray_icon.show()

    def connect_signal_and_slot(self):
        self.ui.comboBox_src_lang.currentIndexChanged.connect(self.slot_translate)
        self.ui.comboBox_dest_lang.currentIndexChanged.connect(self.slot_translate)
        self.ui.comboBox_trans_api.currentIndexChanged.connect(self.slot_translate)
        self.ui.plainTextEdit_src.textChanged.connect(self.slot_text_changed)
        self.ui.pushButton_clear.clicked.connect(self.slot_clear)
        self.ui.pushButton_copy.clicked.connect(self.slot_copy_text)
        self.signal_thread.connect(self.slot_translate)

    def init_customized_ui(self):
        """
        初始化一些自定义的UI
        """
        self.ui.plainTextEdit_src.setPlainText(TEXT_SRC[self.platform])
        self.ui.plainTextEdit_dest.setPlainText(TEXT_DEST[self.platform])

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
        src_lang = self.ui.comboBox_src_lang.currentText()[-2:]  # 获取src语言

        # 空字符或者超过字数限制调用翻译
        if src_text == '' or len(src_text) > max_len or src_text == TEXT_SRC[self.platform]:
            return

        # 格式化文本
        src_text_formatted = misc.format_text(src_text) if self.ui.pushButton_format.isChecked() else src_text
        if src_text != src_text_formatted:
            self.ui.plainTextEdit_src.setPlainText(src_text_formatted)  # 显示格式化后的文本（去换行）

        # 翻译并显示
        api_type = self.ui.comboBox_trans_api.currentText()  # 获取选用的翻译API
        dest_lang = self.ui.comboBox_dest_lang.currentText()[-2:]  # 获取dest语言
        dest_text = self.mytranslator[api_type].trans(src_text_formatted, lang_dict[src_lang],
                                                      lang_dict[dest_lang])  # 翻译
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

    def action(self):
        while True:
            current_time = time.time()
            if self.FLAG and current_time - self.last_trans_time < 2:
                print('子线程: 启动翻译函数')
                self.signal_thread.emit()
            time.sleep(1.5)

    def slot_text_changed(self):
        """
        槽: 文本变化
        """
        self.FLAG = True
        self.last_trans_time = time.time()
