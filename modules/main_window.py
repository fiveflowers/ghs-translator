#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: main_window.py
# @Function: 主窗口

import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication

from modules.configure import Configure
from modules.formatting import TextFormat
from modules.main_window_layout import Ui_MainWindow
from modules.pdf_viewer import PdfViewer
from modules.translator import MyTranslator


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

        self.format = TextFormat()  # 文本格式化
        self.translator = MyTranslator()  # 实例化翻译器
        self.pdf_viewer = PdfViewer()  # 实例化 pdf viewer
        self.ui.gridLayout.addWidget(self.pdf_viewer, 0, 1, 1, 1)  # 在布局中添加 pdf viewer
        self.connect_signal_and_slot()  # 一梭子绑定信号与槽
        self.update_history_from_config()  # 读取历史记录

    def connect_signal_and_slot(self):
        self.pdf_viewer.signal_mouse_release_in_pdf_viewer.connect(
            self.slot_get_selected_text_from_viewer)  # 鼠标释放，获取选中文本
        self.ui.action_open_folder.triggered.connect(self.slot_open_folder)  # 打开文件夹
        self.ui.action_open_file.triggered.connect(self.slot_open_file)  # 打开文件
        self.ui.action_clear_history.triggered.connect(self.slot_clean_history)  # 清空历史
        self.ui.action_close_file.triggered.connect(self.slot_close_file)  # 关闭文件
        self.ui.action_feedback.triggered.connect(self.slot_feedback)  # 问题反馈
        self.ui.plainTextEdit_original_text.textChanged.connect(self.slot_translate)  # 执行翻译
        self.ui.toolButton_font_size_decrease.clicked.connect(self.slot_decrease_font_size)  # 减小翻译区字体
        self.ui.toolButton_font_size_increase.clicked.connect(self.slot_increase_font_size)  # 增大翻译区字体
        self.ui.toolButton_copy.clicked.connect(self.slot_copy_translated_text)  # 翻译
        self.ui.listWidget_history.itemDoubleClicked.connect(self.slot_open_file_from_history)  # 从历史记录打开文件
        self.ui.listWidget_files_in_dir.itemDoubleClicked.connect(self.slot_open_file_from_dir_list)  # 从文件列表中打开文件

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

    def update_file_list_from_dir(self, path_dir):
        self.list_files_filename = []  # 清空内存中的列表信息
        self.list_files_filepath = []  # 清空内存中的列表信息
        files = os.listdir(path_dir)
        for file in files:
            filename_base = file
            if filename_base[-4:] == '.pdf':
                filename = filename_base[:-4]
                filepath = os.path.join(path_dir, filename_base)
                self.list_files_filename.append(filename)
                self.list_files_filepath.append(filepath)
        self.ui.listWidget_files_in_dir.addItems(self.list_files_filename)  # 在侧边栏显示出来

    def slot_get_selected_text_from_viewer(self):
        """
        槽
        获取Viewer中选中的文字，并显示出来
        接受信号：viewer最高的鼠标释放事件
        """
        if self.pdf_viewer.hasSelection():
            raw_text = self.pdf_viewer.selectedText()  # 获得原始文本
            plain_text = self.format.reformat(raw_text)  # 对选中的原始文字进行格式化处理（去除换行连字符）
            if len(plain_text) < self.MAX_CHARACTERS:
                self.ui.plainTextEdit_original_text.setPlainText(plain_text)  # 并显示出来
            else:
                error_message = "警告：单次选中的文字过多，超过了%s，请重新选择翻译文本" % self.MAX_CHARACTERS
                self.ui.plainTextEdit_original_text.setPlainText(error_message)  # 报错

    def slot_translate(self):
        """
        槽
        调用谷歌翻译，并显示结果
        接受信号：待翻译框中有文本变化
        :return: None
        """
        text_to_translate = self.ui.plainTextEdit_original_text.toPlainText()  # 获取待翻译文本
        text_translated = self.translator.translate(text_to_translate, dest='zh-cn').text  # 执行翻译
        self.ui.plainTextEdit_translated_text.setPlainText(text_translated)  # 显示翻译结果

    def slot_open_file(self):
        """
        槽
        打开文件
        接受信号：按钮
        """
        file_path = QFileDialog.getOpenFileName(self, '选择需要打开的PDF文件', './', 'All(*.*);;PDF(*.pdf)', 'PDF(*.pdf)')[0]
        if file_path != '':
            self.pdf_viewer.load_pdf_file(file_path)
            self.ui.sidebar.show()
            self.update_history_from_config()

    def slot_close_file(self):
        """
        槽
        关闭文件，加载起始页面
        接受信号：按钮
        :return: None
        """
        self.pdf_viewer.load_pdf_file('default')

    def slot_open_folder(self):
        """
        槽
        打开文件夹
        接受信号：按钮
        """
        folder_path = QFileDialog.getExistingDirectory(self, '选择需要打开的文件夹', './')
        if folder_path != '':
            self.ui.sidebar.show()
            self.update_file_list_from_dir(folder_path)

    def slot_clean_history(self):
        """
        槽
        清空历史记录
        接受信号：按钮
        :return: None
        """
        config = Configure()
        config.clean_history()
        self.update_history_from_config()  # 更新侧边栏的历史记录

    def slot_open_file_from_history(self, item):
        """
        槽
        从历史记录中打开文件
        接受信号：双击“历史记录”列表中的某个条目
        :param item: 历史记录中选中的条目
        :return: NOne
        """
        for filepath in self.list_history_filepath:
            temp_filename = os.path.basename(filepath)
            if item.text() == temp_filename[:-4].lower():
                self.pdf_viewer.load_pdf_file(filepath)
        self.update_history_from_config()

    def slot_open_file_from_dir_list(self, item):
        """
        槽
        从文件列表中打开文件
        接受信号：双击文件列表中的条目
        :param item: 列表中选中的条目
        :return: None
        """
        for filepath in self.list_files_filepath:
            temp_filename = os.path.basename(filepath)
            if item.text().lower() == temp_filename[:-4].lower():
                self.pdf_viewer.load_pdf_file(filepath)
        self.update_history_from_config()

    def slot_copy_translated_text(self):
        """
        槽
        复制翻译好的文本
        接受信号：按钮
        :return: None
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.plainTextEdit_translated_text.toPlainText())

    def slot_feedback(self):
        """
        槽
        打开问题反馈链接
        接受信号：按钮
        :return: None
        """
        url_feedback = "https://www.yifer.net/app-tech/ghs-translator.html#comments"
        self.pdf_viewer.load_url(url_feedback)

    def slot_increase_font_size(self):
        """
        槽
        增大翻译框内的字体
        接受信号：按钮
        """
        font = QFont()
        self.trans_font_size = min(self.trans_font_size + 1, 30)
        font.setPointSize(self.trans_font_size)
        self.ui.plainTextEdit_original_text.setFont(font)
        self.ui.plainTextEdit_translated_text.setFont(font)

    def slot_decrease_font_size(self):
        """
        槽
        减小翻译框内的字体
        接受信号：按钮
        """
        font = QFont()
        self.trans_font_size = max(self.trans_font_size - 1, 11)
        font.setPointSize(self.trans_font_size)
        self.ui.plainTextEdit_original_text.setFont(font)
        self.ui.plainTextEdit_translated_text.setFont(font)
