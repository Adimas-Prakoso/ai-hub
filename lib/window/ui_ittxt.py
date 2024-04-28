# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ittxtHeRMae.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QPixmap, )
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_ImageToText(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(160, 166, 255);\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(87, 90, 138);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(4, 4, 4, 4)
        self.path = QLabel(self.frame_7)
        self.path.setObjectName(u"path")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.path.setFont(font)

        self.gridLayout_9.addWidget(self.path, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_7, 1, 0, 1, 1)

        self.select_file = QPushButton(self.frame_4)
        self.select_file.setObjectName(u"select_file")
        self.select_file.setMinimumSize(QSize(0, 40))
        self.select_file.setMaximumSize(QSize(90, 70))
        font1 = QFont()
        font1.setBold(True)
        self.select_file.setFont(font1)
        self.select_file.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.select_file, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(87, 90, 138);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.hasil = QTextEdit(self.frame_8)
        self.hasil.setObjectName(u"hasil")
        self.hasil.setFont(font)
        self.hasil.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hasil.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hasil.setReadOnly(True)

        self.gridLayout_8.addWidget(self.hasil, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_8, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 1, 0, 1, 1)

        self.generate = QPushButton(self.frame_5)
        self.generate.setObjectName(u"generate")
        self.generate.setMinimumSize(QSize(0, 40))
        self.generate.setFont(font1)
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.gridLayout_5.addWidget(self.generate, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"background-color: rgb(73, 76, 116);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"./res/image/[removal.ai]_a84c2b95-b237-4c04-add0-3ab8754597be-aihub_PDDORY.png"))
        self.label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_title = QLabel(self.frame_2)
        self.label_title.setObjectName(u"label_title")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_title.setFont(font2)
        self.label_title.setStyleSheet(u"color: rgb(59, 117, 176)")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_title, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(478, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.close_btn = QPushButton(self.frame_2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setFont(font2)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"border-radius: 10px")

        self.gridLayout_3.addWidget(self.close_btn, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.path.setText("")
        self.select_file.setText(QCoreApplication.translate("MainWindow", u"SELECT FILE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Images:", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.label.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"AI HUB", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
    # retranslateUi

