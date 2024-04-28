# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'itiyCUWss.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QPixmap, )
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
    QLabel, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_ITI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QSize(900, 500))
        MainWindow.setMaximumSize(QSize(900, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.centralwidget.setMaximumSize(QSize(900, 500))
        self.gridLayout = QGridLayout(self.centralwidget)
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
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setStyleSheet(u"background-color: rgb(73, 76, 116);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.header)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 3, 9, 3)
        self.close_btn = QPushButton(self.header)
        self.close_btn.setObjectName(u"close_btn")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"border-radius: 10px")

        self.gridLayout_4.addWidget(self.close_btn, 0, 3, 1, 1)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"./res/image/[removal.ai]_a84c2b95-b237-4c04-add0-3ab8754597be-aihub_PDDORY.png"))
        self.label.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(738, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_title = QLabel(self.header)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(59, 117, 176)")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_title, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(84, 87, 134);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.hasil = QLabel(self.frame_4)
        self.hasil.setObjectName(u"hasil")
        self.hasil.setMaximumSize(QSize(408, 408))
        self.hasil.setScaledContents(True)

        self.gridLayout_6.addWidget(self.hasil, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(160, 166, 255);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 410, 367))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 30))
        self.frame_8.setStyleSheet(u"background-color: rgb(87, 90, 138);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.cpu = QRadioButton(self.frame_8)
        self.cpu.setObjectName(u"cpu")
        font1 = QFont()
        font1.setBold(True)
        self.cpu.setFont(font1)
        self.cpu.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.cpu, 0, 1, 1, 1)

        self.cuda = QRadioButton(self.frame_8)
        self.cuda.setObjectName(u"cuda")
        self.cuda.setFont(font1)
        self.cuda.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.cuda, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_8, 1, 0, 1, 3)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.frame_7, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(6)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.models = QComboBox(self.frame_5)
        self.models.setObjectName(u"models")
        self.models.setMinimumSize(QSize(0, 30))
        self.models.setFont(font2)
        self.models.setCursor(QCursor(Qt.PointingHandCursor))
        self.models.setStyleSheet(u"background-color: rgb(87, 90, 138);")
        self.models.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.models.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_8.addWidget(self.models, 1, 0, 1, 2)


        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 190))
        self.frame_9.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setStyleSheet(u"background-color: rgb(87, 90, 138);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.prompt = QTextEdit(self.frame_10)
        self.prompt.setObjectName(u"prompt")
        self.prompt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.prompt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_12.addWidget(self.prompt, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_10, 1, 0, 1, 3)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.frame_9, 3, 0, 1, 1)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.frame_11.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(259, 16777215))
        self.frame_12.setStyleSheet(u"background-color: rgb(87, 90, 138);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(4, 4, 4, 4)
        self.path = QLabel(self.frame_12)
        self.path.setObjectName(u"path")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.path.setFont(font3)

        self.gridLayout_14.addWidget(self.path, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_12, 2, 0, 1, 2)

        self.select = QPushButton(self.frame_11)
        self.select.setObjectName(u"select")
        self.select.setMinimumSize(QSize(127, 30))
        self.select.setFont(font1)
        self.select.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.gridLayout_13.addWidget(self.select, 2, 2, 1, 1)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 3)


        self.gridLayout_7.addWidget(self.frame_11, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.generate = QPushButton(self.frame_2)
        self.generate.setObjectName(u"generate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy1)
        self.generate.setMinimumSize(QSize(0, 35))
        self.generate.setFont(font2)
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"background-color: rgb(85, 255, 255);")

        self.gridLayout_5.addWidget(self.generate, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)


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
        self.hasil.setText("")
        self.cpu.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cuda.setText(QCoreApplication.translate("MainWindow", u"CUDA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" Render Method:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  Models:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Prompt:", None))
        self.path.setText("")
        self.select.setText(QCoreApplication.translate("MainWindow", u"SELECT IMAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" Select Image:", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
    # retranslateUi

