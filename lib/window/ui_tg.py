# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tgJAylve.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QPixmap, )
from PySide6.QtWidgets import (QAbstractScrollArea, QFrame, QGridLayout,
    QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_TextGen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QSize(500, 600))
        MainWindow.setMaximumSize(QSize(500, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 600))
        self.centralwidget.setMaximumSize(QSize(500, 600))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
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
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setStyleSheet(u"background-color: rgb(73, 76, 116);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 3, 9, 3)
        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"border-radius: 10px")

        self.gridLayout_4.addWidget(self.close_btn, 0, 3, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"./res/image/[removal.ai]_a84c2b95-b237-4c04-add0-3ab8754597be-aihub_PDDORY.png"))
        self.label.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(738, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_title = QLabel(self.frame_3)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(59, 117, 176)")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_title, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.generate = QPushButton(self.frame_2)
        self.generate.setObjectName(u"generate")
        self.generate.setMinimumSize(QSize(0, 40))
        self.generate.setMaximumSize(QSize(16777215, 40))
        self.generate.setFont(font)
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(85, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.generate, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(160, 166, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 80))
        self.frame_6.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 35))
        self.frame_8.setStyleSheet(u"background-color: rgb(84, 87, 134);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(9, 9, 9, 9)
        self.apis = QRadioButton(self.frame_8)
        self.apis.setObjectName(u"apis")
        font2 = QFont()
        font2.setBold(True)
        self.apis.setFont(font2)

        self.gridLayout_8.addWidget(self.apis, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_8, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(84, 87, 134);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.text = QTextEdit(self.frame_9)
        self.text.setObjectName(u"text")
        self.text.setFont(font2)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.text.setReadOnly(False)

        self.gridLayout_10.addWidget(self.text, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_9, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close_btn.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.label.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"AI HUB", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" Render Method:", None))
        self.apis.setText(QCoreApplication.translate("MainWindow", u"API's", None))
        self.text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" Content:", None))
    # retranslateUi

