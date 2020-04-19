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
        MainWindow.resize(1254, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 800))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.transbar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transbar.sizePolicy().hasHeightForWidth())
        self.transbar.setSizePolicy(sizePolicy)
        self.transbar.setMaximumSize(QtCore.QSize(400, 16777215))
        self.transbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transbar.setObjectName("transbar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.transbar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_font_size_increase = QtWidgets.QToolButton(self.transbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_font_size_increase.sizePolicy().hasHeightForWidth())
        self.toolButton_font_size_increase.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/images/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_font_size_increase.setIcon(icon)
        self.toolButton_font_size_increase.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_font_size_increase.setObjectName("toolButton_font_size_increase")
        self.horizontalLayout.addWidget(self.toolButton_font_size_increase)
        self.toolButton_font_size_decrease = QtWidgets.QToolButton(self.transbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_font_size_decrease.sizePolicy().hasHeightForWidth())
        self.toolButton_font_size_decrease.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resource/images/zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_font_size_decrease.setIcon(icon1)
        self.toolButton_font_size_decrease.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_font_size_decrease.setObjectName("toolButton_font_size_decrease")
        self.horizontalLayout.addWidget(self.toolButton_font_size_decrease)
        self.toolButton_copy = QtWidgets.QToolButton(self.transbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_copy.sizePolicy().hasHeightForWidth())
        self.toolButton_copy.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resource/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_copy.setIcon(icon2)
        self.toolButton_copy.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_copy.setObjectName("toolButton_copy")
        self.horizontalLayout.addWidget(self.toolButton_copy)
        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.label_original_text = QtWidgets.QLabel(self.transbar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_original_text.setFont(font)
        self.label_original_text.setObjectName("label_original_text")
        self.gridLayout_3.addWidget(self.label_original_text, 1, 0, 1, 1)
        self.plainTextEdit_original_text = QtWidgets.QPlainTextEdit(self.transbar)
        self.plainTextEdit_original_text.setEnabled(True)
        self.plainTextEdit_original_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_original_text.setFont(font)
        self.plainTextEdit_original_text.setAcceptDrops(False)
        self.plainTextEdit_original_text.setPlainText("")
        self.plainTextEdit_original_text.setCenterOnScroll(False)
        self.plainTextEdit_original_text.setObjectName("plainTextEdit_original_text")
        self.gridLayout_3.addWidget(self.plainTextEdit_original_text, 2, 0, 1, 1)
        self.plainTextEdit_translated_text = QtWidgets.QPlainTextEdit(self.transbar)
        self.plainTextEdit_translated_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_translated_text.setFont(font)
        self.plainTextEdit_translated_text.setAcceptDrops(False)
        self.plainTextEdit_translated_text.setPlainText("")
        self.plainTextEdit_translated_text.setObjectName("plainTextEdit_translated_text")
        self.gridLayout_3.addWidget(self.plainTextEdit_translated_text, 4, 0, 1, 1)
        self.label_translated_text = QtWidgets.QLabel(self.transbar)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_translated_text.setFont(font)
        self.label_translated_text.setObjectName("label_translated_text")
        self.gridLayout_3.addWidget(self.label_translated_text, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.transbar, 0, 2, 1, 1)
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sidebar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_files_in_dir = QtWidgets.QListWidget(self.sidebar)
        self.listWidget_files_in_dir.setEnabled(True)
        self.listWidget_files_in_dir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_files_in_dir.setFont(font)
        self.listWidget_files_in_dir.setObjectName("listWidget_files_in_dir")
        self.gridLayout_2.addWidget(self.listWidget_files_in_dir, 1, 0, 1, 1)
        self.label_history = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_history.setFont(font)
        self.label_history.setObjectName("label_history")
        self.gridLayout_2.addWidget(self.label_history, 2, 0, 1, 1)
        self.label_folder = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_folder.setFont(font)
        self.label_folder.setObjectName("label_folder")
        self.gridLayout_2.addWidget(self.label_folder, 0, 0, 1, 1)
        self.listWidget_history = QtWidgets.QListWidget(self.sidebar)
        self.listWidget_history.setEnabled(True)
        self.listWidget_history.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_history.setFont(font)
        self.listWidget_history.setObjectName("listWidget_history")
        self.gridLayout_2.addWidget(self.listWidget_history, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.sidebar, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 29))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./resource/images/file_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_file.setIcon(icon3)
        self.action_open_file.setObjectName("action_open_file")
        self.action_open_folder = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./resource/images/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_folder.setIcon(icon4)
        self.action_open_folder.setObjectName("action_open_folder")
        self.action_close_file = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./resource/images/file_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close_file.setIcon(icon5)
        self.action_close_file.setObjectName("action_close_file")
        self.action_clear_history = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./resource/images/clear_history.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clear_history.setIcon(icon6)
        self.action_clear_history.setObjectName("action_clear_history")
        self.action_app_exit = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./resource/images/app_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_app_exit.setIcon(icon7)
        self.action_app_exit.setObjectName("action_app_exit")
        self.action_window_maximize = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./resource/images/window_maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_window_maximize.setIcon(icon8)
        self.action_window_maximize.setObjectName("action_window_maximize")
        self.action_window_reset = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./resource/images/window_reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_window_reset.setIcon(icon9)
        self.action_window_reset.setObjectName("action_window_reset")
        self.action_sidebar_show = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./resource/images/sidebar_show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_sidebar_show.setIcon(icon10)
        self.action_sidebar_show.setObjectName("action_sidebar_show")
        self.action_sidebar_hide = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./resource/images/sidebar_hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_sidebar_hide.setIcon(icon11)
        self.action_sidebar_hide.setObjectName("action_sidebar_hide")
        self.action_paper_assistant = QtWidgets.QAction(MainWindow)
        self.action_paper_assistant.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./resource/images/paper-assistant.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_paper_assistant.setIcon(icon12)
        self.action_paper_assistant.setObjectName("action_paper_assistant")
        self.action_document_translate = QtWidgets.QAction(MainWindow)
        self.action_document_translate.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./resource/images/file_translate.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_document_translate.setIcon(icon13)
        self.action_document_translate.setObjectName("action_document_translate")
        self.action_app_about = QtWidgets.QAction(MainWindow)
        self.action_app_about.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./resource/images/app_about.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_app_about.setIcon(icon14)
        self.action_app_about.setObjectName("action_app_about")
        self.action_feedback = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./resource/images/feedback.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_feedback.setIcon(icon15)
        self.action_feedback.setObjectName("action_feedback")
        self.menu_file.addAction(self.action_open_file)
        self.menu_file.addAction(self.action_open_folder)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close_file)
        self.menu_file.addAction(self.action_clear_history)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_app_exit)
        self.menu_view.addAction(self.action_window_maximize)
        self.menu_view.addAction(self.action_window_reset)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_sidebar_show)
        self.menu_view.addAction(self.action_sidebar_hide)
        self.menu_tools.addAction(self.action_paper_assistant)
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
        self.toolBar.addAction(self.action_sidebar_show)
        self.toolBar.addAction(self.action_sidebar_hide)
        self.toolBar.addAction(self.action_window_maximize)
        self.toolBar.addAction(self.action_window_reset)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_paper_assistant)
        self.toolBar.addAction(self.action_document_translate)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.action_app_exit.triggered.connect(MainWindow.close)
        self.action_window_maximize.triggered.connect(MainWindow.showMaximized)
        self.action_window_reset.triggered.connect(MainWindow.showNormal)
        self.action_sidebar_hide.triggered.connect(self.sidebar.hide)
        self.action_sidebar_show.triggered.connect(self.sidebar.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "根号三翻译器（GHS Translator） - 论文小助手"))
        self.toolButton_font_size_increase.setToolTip(_translate("MainWindow", "增大字体"))
        self.toolButton_font_size_increase.setText(_translate("MainWindow", "..."))
        self.toolButton_font_size_decrease.setToolTip(_translate("MainWindow", "减小字体"))
        self.toolButton_font_size_decrease.setText(_translate("MainWindow", "..."))
        self.toolButton_copy.setToolTip(_translate("MainWindow", "复制翻译结果"))
        self.toolButton_copy.setText(_translate("MainWindow", "..."))
        self.label_original_text.setText(_translate("MainWindow", "翻译文本"))
        self.plainTextEdit_original_text.setToolTip(_translate("MainWindow", "可自由修改文本，修改后将自动翻译"))
        self.plainTextEdit_translated_text.setToolTip(_translate("MainWindow", "基于谷歌翻译"))
        self.label_translated_text.setText(_translate("MainWindow", "翻译结果"))
        self.sidebar.setToolTip(_translate("MainWindow", "侧边栏，可以通过上方工具栏隐藏"))
        self.label_history.setText(_translate("MainWindow", "最近文档"))
        self.label_folder.setText(_translate("MainWindow", "当前目录"))
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
        self.action_window_maximize.setText(_translate("MainWindow", "窗口最大化"))
        self.action_window_reset.setText(_translate("MainWindow", "窗口正常化"))
        self.action_sidebar_show.setText(_translate("MainWindow", "显示侧边栏"))
        self.action_sidebar_hide.setText(_translate("MainWindow", "隐藏侧边栏"))
        self.action_paper_assistant.setText(_translate("MainWindow", "写作助手"))
        self.action_document_translate.setText(_translate("MainWindow", "文档翻译"))
        self.action_app_about.setText(_translate("MainWindow", "软件信息"))
        self.action_feedback.setText(_translate("MainWindow", "意见反馈"))
