# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLTArol.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 660)
        MainWindow.setMinimumSize(QSize(920, 660))
        MainWindow.setMaximumSize(QSize(920, 660))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(920, 660))
        self.centralwidget.setMaximumSize(QSize(920, 660))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(906, 646))
        self.frame.setMaximumSize(QSize(906, 646))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 45))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(88, 91, 140);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 5, 10, 5)
        self.horizontalSpacer = QSpacerItem(680, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(40, 16777215))
        font = QFont()
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px")

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(40, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-radius: 10px")

        self.gridLayout_3.addWidget(self.pushButton, 0, 5, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"./res/image/[removal.ai]_a84c2b95-b237-4c04-add0-3ab8754597be-aihub_PDDORY.png"))
        self.label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_title = QLabel(self.frame_2)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(59, 117, 176)")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_title, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setStyleSheet(u"background-color: rgb(63, 65, 100);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(93, 97, 148);")

        self.gridLayout_7.addWidget(self.label_3, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(640, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(93, 97, 148);")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_8, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 906, 762))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(888, 250))
        self.frame_3.setMaximumSize(QSize(888, 250))
        self.frame_3.setStyleSheet(u"background-color: rgb(75, 78, 120);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 220))
        self.frame_5.setMaximumSize(QSize(200, 220))
        self.frame_5.setStyleSheet(u"background-color: rgb(155, 161, 247);\n"
"border-radius: 10px")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(4)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border-radius: 10px")
        self.label_4.setPixmap(QPixmap(u"./res/image/f1VQ7f7nCK.jpg"))
        self.label_4.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.tti_button = QPushButton(self.frame_5)
        self.tti_button.setObjectName(u"tti_button")
        self.tti_button.setMinimumSize(QSize(0, 20))
        self.tti_button.setMaximumSize(QSize(16777215, 20))
        self.tti_button.setFont(font)
        self.tti_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.tti_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_8.addWidget(self.tti_button, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 220))
        self.frame_6.setMaximumSize(QSize(200, 220))
        self.frame_6.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(4)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gif_lable = QLabel(self.frame_6)
        self.gif_lable.setObjectName(u"gif_lable")

        self.gridLayout_9.addWidget(self.gif_lable, 0, 0, 1, 1)

        self.ttv_button = QPushButton(self.frame_6)
        self.ttv_button.setObjectName(u"ttv_button")
        self.ttv_button.setMinimumSize(QSize(0, 20))
        self.ttv_button.setMaximumSize(QSize(16777215, 20))
        self.ttv_button.setFont(font)
        self.ttv_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ttv_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_9.addWidget(self.ttv_button, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 220))
        self.frame_7.setMaximumSize(QSize(200, 220))
        self.frame_7.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(4)
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u"./res/image/Screenshot 2023-11-27 213552.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)

        self.tttxt_button = QPushButton(self.frame_7)
        self.tttxt_button.setObjectName(u"tttxt_button")
        self.tttxt_button.setMinimumSize(QSize(0, 20))
        self.tttxt_button.setMaximumSize(QSize(16777215, 20))
        self.tttxt_button.setFont(font)
        self.tttxt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.tttxt_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_10.addWidget(self.tttxt_button, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_7, 0, 2, 1, 1)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(200, 220))
        self.frame_10.setMaximumSize(QSize(200, 220))
        self.frame_10.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(4)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"./res/image/219588f3-5421-4f51-b40d-ceeb90d26875.jpg"))
        self.label_6.setScaledContents(True)

        self.gridLayout_11.addWidget(self.label_6, 0, 0, 1, 1)

        self.iti_button = QPushButton(self.frame_10)
        self.iti_button.setObjectName(u"iti_button")
        self.iti_button.setMinimumSize(QSize(0, 20))
        self.iti_button.setMaximumSize(QSize(16777215, 20))
        self.iti_button.setFont(font)
        self.iti_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.iti_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_11.addWidget(self.iti_button, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_10, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(888, 250))
        self.frame_4.setMaximumSize(QSize(888, 250))
        self.frame_4.setStyleSheet(u"background-color: rgb(75, 78, 120);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(200, 220))
        self.frame_12.setMaximumSize(QSize(200, 220))
        self.frame_12.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setVerticalSpacing(4)
        self.gridLayout_14.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"./res/image/OIP2.jpg"))
        self.label_9.setScaledContents(True)

        self.gridLayout_14.addWidget(self.label_9, 0, 0, 1, 1)

        self.ttc_button = QPushButton(self.frame_12)
        self.ttc_button.setObjectName(u"ttc_button")
        self.ttc_button.setMinimumSize(QSize(0, 20))
        self.ttc_button.setMaximumSize(QSize(16777215, 20))
        self.ttc_button.setFont(font)
        self.ttc_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ttc_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_14.addWidget(self.ttc_button, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_12, 0, 3, 1, 1)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 220))
        self.frame_13.setMaximumSize(QSize(200, 220))
        self.frame_13.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(0)
        self.gridLayout_15.setVerticalSpacing(4)
        self.gridLayout_15.setContentsMargins(5, 5, 5, 5)
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u"./res/image/image_processing20201015-17815-ipphgn.jpg"))
        self.label_10.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_10, 0, 0, 1, 1)

        self.ttm_button = QPushButton(self.frame_13)
        self.ttm_button.setObjectName(u"ttm_button")
        self.ttm_button.setMinimumSize(QSize(0, 20))
        self.ttm_button.setMaximumSize(QSize(16777215, 20))
        self.ttm_button.setFont(font)
        self.ttm_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ttm_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_15.addWidget(self.ttm_button, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_13, 0, 4, 1, 1)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(200, 220))
        self.frame_11.setMaximumSize(QSize(200, 220))
        self.frame_11.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(4)
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u"./res/image/thumbnail.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 1)

        self.tg_button = QPushButton(self.frame_11)
        self.tg_button.setObjectName(u"tg_button")
        self.tg_button.setMinimumSize(QSize(0, 20))
        self.tg_button.setMaximumSize(QSize(16777215, 20))
        self.tg_button.setFont(font)
        self.tg_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.tg_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_13.addWidget(self.tg_button, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_11, 0, 2, 1, 1)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 220))
        self.frame_9.setMaximumSize(QSize(200, 220))
        self.frame_9.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setVerticalSpacing(4)
        self.gridLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u"./res/image/OIP.jpg"))
        self.label_7.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_7, 0, 0, 1, 1)

        self.qa_buttton = QPushButton(self.frame_9)
        self.qa_buttton.setObjectName(u"qa_buttton")
        self.qa_buttton.setMinimumSize(QSize(0, 20))
        self.qa_buttton.setMaximumSize(QSize(16777215, 20))
        self.qa_buttton.setFont(font)
        self.qa_buttton.setCursor(QCursor(Qt.PointingHandCursor))
        self.qa_buttton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_12.addWidget(self.qa_buttton, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_9, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(888, 250))
        self.frame_14.setMaximumSize(QSize(888, 250))
        self.frame_14.setStyleSheet(u"background-color: rgb(75, 78, 120);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_14)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(200, 220))
        self.frame_15.setMaximumSize(QSize(200, 220))
        self.frame_15.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_15)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(0)
        self.gridLayout_17.setVerticalSpacing(4)
        self.gridLayout_17.setContentsMargins(5, 5, 5, 5)
        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u"./res/image/Screenshot 2023-11-28 194152.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout_17.addWidget(self.label_11, 0, 0, 1, 1)

        self.tts_button = QPushButton(self.frame_15)
        self.tts_button.setObjectName(u"tts_button")
        self.tts_button.setMinimumSize(QSize(0, 20))
        self.tts_button.setMaximumSize(QSize(16777215, 20))
        self.tts_button.setFont(font)
        self.tts_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.tts_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_17.addWidget(self.tts_button, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_15, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(200, 220))
        self.frame_16.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_16)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setVerticalSpacing(4)
        self.gridLayout_18.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u"./res/image/vecteezy_openai-chatgpt-logo-icon_24558805.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout_18.addWidget(self.label_12, 0, 0, 1, 1)

        self.con_button = QPushButton(self.frame_16)
        self.con_button.setObjectName(u"con_button")
        self.con_button.setMinimumSize(QSize(0, 20))
        self.con_button.setMaximumSize(QSize(16777215, 20))
        self.con_button.setFont(font)
        self.con_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.con_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_18.addWidget(self.con_button, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_16, 0, 1, 1, 1)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(200, 220))
        self.frame_17.setMaximumSize(QSize(200, 220))
        self.frame_17.setStyleSheet(u"background-color: rgb(155, 161, 247);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_17)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(0)
        self.gridLayout_19.setVerticalSpacing(4)
        self.gridLayout_19.setContentsMargins(5, 5, 5, 5)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u"./res/image/Screenshot 2023-11-28 203936.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_19.addWidget(self.label_13, 0, 0, 1, 1)

        self.im_button = QPushButton(self.frame_17)
        self.im_button.setObjectName(u"im_button")
        self.im_button.setMinimumSize(QSize(0, 20))
        self.im_button.setMaximumSize(QSize(16777215, 20))
        self.im_button.setFont(font)
        self.im_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.im_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 2, 2);\n"
"}")

        self.gridLayout_19.addWidget(self.im_button, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_17, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_14, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)
        #self.tti_button.clicked.connect(self.open_tti_window)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.label.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"AI HUB", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Created By: Adimas Prakoso", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"VERSION: 1.0", None))
        self.label_4.setText("")
        self.tti_button.setText(QCoreApplication.translate("MainWindow", u"Text To Image", None))
        self.gif_lable.setText("")
        self.ttv_button.setText(QCoreApplication.translate("MainWindow", u"Text To Video", None))
        self.label_5.setText("")
        self.tttxt_button.setText(QCoreApplication.translate("MainWindow", u"Image To Text", None))
        self.label_6.setText("")
        self.iti_button.setText(QCoreApplication.translate("MainWindow", u"Image To Image", None))
        self.label_9.setText("")
        self.ttc_button.setText(QCoreApplication.translate("MainWindow", u"Text To Code", None))
        self.label_10.setText("")
        self.ttm_button.setText(QCoreApplication.translate("MainWindow", u"Text To Music", None))
        self.label_8.setText("")
        self.tg_button.setText(QCoreApplication.translate("MainWindow", u"Text Generation", None))
        self.label_7.setText("")
        self.qa_buttton.setText(QCoreApplication.translate("MainWindow", u"Question Answering", None))
        self.label_11.setText("")
        self.tts_button.setText(QCoreApplication.translate("MainWindow", u"Text To Speech", None))
        self.label_12.setText("")
        self.con_button.setText(QCoreApplication.translate("MainWindow", u"Conversation", None))
        self.label_13.setText("")
        self.im_button.setText(QCoreApplication.translate("MainWindow", u"Image Maker", None))
    # retranslateUi

