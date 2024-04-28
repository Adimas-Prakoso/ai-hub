# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashreMUII.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtGui import (QFont, QPixmap, )
from PySide6.QtWidgets import (QFrame, QLabel, QProgressBar, QVBoxLayout, QWidget)

class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        if not SplashWindow.objectName():
            SplashWindow.setObjectName(u"SplashWindow")
        SplashWindow.resize(700, 400)
        self.centralwidget = QWidget(SplashWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setEnabled(True)
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 150, 681, 61))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(77, 232, 232)")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 270, 611, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 144, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 11px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 11px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.988636, y2:0.511273, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 310, 681, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"color: rgb(98, 141, 164)")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(510, 340, 151, 31))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(55, 195, 255);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 60, 100, 100))
        self.label.setPixmap(QPixmap(u"./res/image/[removal.ai]_a84c2b95-b237-4c04-add0-3ab8754597be-aihub_PDDORY.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashWindow)

        QMetaObject.connectSlotsByName(SplashWindow)
    # setupUi

    def retranslateUi(self, SplashWindow):
        SplashWindow.setWindowTitle(QCoreApplication.translate("SplashWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashWindow", u"AI HUB", None))
        self.label_loading.setText(QCoreApplication.translate("SplashWindow", u"Loading....", None))
        self.label_credits.setText(QCoreApplication.translate("SplashWindow", u"<strong>Created By:</strong> Adimas Prakoso", None))
        self.label.setText("")
    # retranslateUi

