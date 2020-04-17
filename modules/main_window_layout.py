# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 719)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 29))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(36, 36))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_open_file = QtWidgets.QAction(MainWindow)
        self.action_open_file.setObjectName("action_open_file")
        self.action_open_folder = QtWidgets.QAction(MainWindow)
        self.action_open_folder.setObjectName("action_open_folder")
        self.action_close_file = QtWidgets.QAction(MainWindow)
        self.action_close_file.setObjectName("action_close_file")
        self.action_clear_history = QtWidgets.QAction(MainWindow)
        self.action_clear_history.setObjectName("action_clear_history")
        self.action_app_exit = QtWidgets.QAction(MainWindow)
        self.action_app_exit.setObjectName("action_app_exit")
        self.action_window_maximize = QtWidgets.QAction(MainWindow)
        self.action_window_maximize.setObjectName("action_window_maximize")
        self.action_window_minimize = QtWidgets.QAction(MainWindow)
        self.action_window_minimize.setObjectName("action_window_minimize")
        self.action_sidebar_show = QtWidgets.QAction(MainWindow)
        self.action_sidebar_show.setObjectName("action_sidebar_show")
        self.action_sidebar_hide = QtWidgets.QAction(MainWindow)
        self.action_sidebar_hide.setObjectName("action_sidebar_hide")
        self.action_paperwriting_helper = QtWidgets.QAction(MainWindow)
        self.action_paperwriting_helper.setObjectName("action_paperwriting_helper")
        self.action_document_translate = QtWidgets.QAction(MainWindow)
        self.action_document_translate.setObjectName("action_document_translate")
        self.action_app_about = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/images/app_about.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_app_about.setIcon(icon)
        self.action_app_about.setObjectName("action_app_about")
        self.action_feedback = QtWidgets.QAction(MainWindow)
        self.action_feedback.setObjectName("action_feedback")
        self.menu_file.addAction(self.action_open_file)
        self.menu_file.addAction(self.action_open_folder)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close_file)
        self.menu_file.addAction(self.action_clear_history)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_app_exit)
        self.menu_view.addAction(self.action_window_maximize)
        self.menu_view.addAction(self.action_window_minimize)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_sidebar_show)
        self.menu_view.addAction(self.action_sidebar_hide)
        self.menu_tools.addAction(self.action_paperwriting_helper)
        self.menu_tools.addAction(self.action_document_translate)
        self.menu_about.addAction(self.action_app_about)
        self.menu_about.addAction(self.action_feedback)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.toolBar.addAction(self.action_open_file)
        self.toolBar.addAction(self.action_open_folder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_close_file)
        self.toolBar.addAction(self.action_clear_history)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_window_maximize)
        self.toolBar.addAction(self.action_window_minimize)
        self.toolBar.addAction(self.action_sidebar_show)
        self.toolBar.addAction(self.action_sidebar_hide)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_paperwriting_helper)
        self.toolBar.addAction(self.action_document_translate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_feedback)

        self.retranslateUi(MainWindow)
        self.action_app_exit.triggered.connect(MainWindow.close)
        self.action_window_maximize.triggered.connect(MainWindow.showMaximized)
        self.action_window_minimize.triggered.connect(MainWindow.showNormal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "根号三 翻译器 - 论文助手 （Paper Assistant）"))
        self.menu_file.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_view.setTitle(_translate("MainWindow", "界面(&V)"))
        self.menu_tools.setTitle(_translate("MainWindow", "工具(&T)"))
        self.menu_about.setTitle(_translate("MainWindow", "关于(&A)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_open_file.setText(_translate("MainWindow", "打开文件"))
        self.action_open_folder.setText(_translate("MainWindow", "打开文件夹"))
        self.action_close_file.setText(_translate("MainWindow", "关闭文件"))
        self.action_clear_history.setText(_translate("MainWindow", "清除历史"))
        self.action_app_exit.setText(_translate("MainWindow", "退出程序"))
        self.action_window_maximize.setText(_translate("MainWindow", "最大化"))
        self.action_window_minimize.setText(_translate("MainWindow", "最小化"))
        self.action_sidebar_show.setText(_translate("MainWindow", "显示侧边栏"))
        self.action_sidebar_hide.setText(_translate("MainWindow", "隐藏侧边栏"))
        self.action_paperwriting_helper.setText(_translate("MainWindow", "写作助手"))
        self.action_document_translate.setText(_translate("MainWindow", "文档翻译"))
        self.action_app_about.setText(_translate("MainWindow", "软件信息"))
        self.action_feedback.setText(_translate("MainWindow", "意见反馈"))