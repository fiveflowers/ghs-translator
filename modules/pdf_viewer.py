#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: pdf_viewer.py
# @Function: 基于QWebEngineView的PDF浏览器

import os

from PyQt5.QtCore import pyqtSignal, QUrl, QEvent
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QSizePolicy

from modules.configure import Configure
from modules.cross_platform import CrossPlatform


class PdfViewer(QWebEngineView):
    signal_mouse_release_in_pdf_viewer = pyqtSignal()  # 鼠标释放信号

    def __init__(self):
        super(PdfViewer, self).__init__()
        self.setObjectName("pdf_viewer")
        self.child_event_tracker = None  # 用于检测鼠标事件(属于QWebEngineView子事件)
        self.default_viewer = "file:///" + os.path.join(os.getcwd(), "pdf.js", 'web', 'viewer.html')  # 默认pdf viewer路径
        self.set_size_policy()  # 设置尺寸策略
        self.load_pdf_file('default')  # 初始化viewer

    def set_size_policy(self):
        """
        设置尺寸策略，基于Designer
        :return: None
        """
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(2)
        size_policy.setVerticalStretch(0)
        self.setSizePolicy(size_policy)

    def load_pdf_file(self, pdf_file_path):
        """
        加载用户自定义pdf文件
        并添加到历史记录文件中
        :param pdf_file_path: pdf文件路径，若为‘default’，则加载默认页面
        :return: None
        """
        if pdf_file_path == 'default':
            path = CrossPlatform.path_converter(self.default_viewer)
            self.setUrl(QUrl(path))
        else:  # 打开用户指定的pdf文件
            config = Configure()
            filename_base = os.path.basename(pdf_file_path)  # basename是带有文件扩展名的
            filename = filename_base[:-4]  # 获得无扩展名的文件名
            config.add_history(filename, pdf_file_path)  # 添加历史记录
            path = CrossPlatform.path_converter(self.default_viewer + '?file=' + pdf_file_path)
            self.setUrl(QUrl(path))

    def event(self, e):
        """
        Detect child add event, as QWebEngineView do not capture mouse event directly,
        the child layer child_event_tracker is implicitly added to QWebEngineView and we track mouse event through the child_event_tracker
        :param e: QEvent
        :return: super().event(e)
        """
        if self.child_event_tracker is None:
            if e.type() == QEvent.ChildAdded and e.child().isWidgetType():
                self.child_event_tracker = e.child()
                self.child_event_tracker.installEventFilter(self)
        return super().event(e)

    def eventFilter(self, source, event):
        """
        检测viewer中的鼠标释放事件，并释放信号
        :param source: viewer
        :param event: 鼠标事件
        :return:
        """
        if event.type() == QEvent.MouseButtonRelease and source is self.child_event_tracker:
            self.signal_mouse_release_in_pdf_viewer.emit()  # 释放信号
            print("鼠标信号已发送...")
        return super().eventFilter(source, event)
