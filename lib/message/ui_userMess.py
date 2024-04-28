# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userMessCzbSTd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QAbstractScrollArea, QFrame, QGridLayout,
    QLabel, QSizePolicy, QTextEdit, )

class Ui_Chats(object):
    def setupUi(self, Chats):
        if not Chats.objectName():
            Chats.setObjectName(u"Chats")
        Chats.resize(640, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Chats.sizePolicy().hasHeightForWidth())
        Chats.setSizePolicy(sizePolicy)
        Chats.setMinimumSize(QSize(0, 100))
        Chats.setMaximumSize(QSize(16777215, 100))
        Chats.setStyleSheet(u"QWidget{\n"
"background-color: rgb(160, 166, 255);\n"
"}")
        self.gridLayout = QGridLayout(Chats)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Chats)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.images = QLabel(self.frame)
        self.images.setObjectName(u"images")
        self.images.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.images, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Chats)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit.setLineWrapColumnOrWidth(0)
        self.textEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)


        self.retranslateUi(Chats)

        QMetaObject.connectSlotsByName(Chats)
    # setupUi

    def retranslateUi(self, Chats):
        Chats.setWindowTitle(QCoreApplication.translate("Chats", u"Form", None))
        self.images.setText("")
        self.textEdit.setPlaceholderText("")
    # retranslateUi

