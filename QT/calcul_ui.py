# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculTKKPzY.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QPushButton, QStatusBar, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(297, 494)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_del = QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName(u"pushButton_del")
        self.pushButton_del.setGeometry(QRect(220, 130, 61, 61))
        self.pushButton_num = QPushButton(self.centralwidget)
        self.pushButton_num.setObjectName(u"pushButton_num")
        self.pushButton_num.setGeometry(QRect(220, 200, 61, 61))
        self.pushButton_minus = QPushButton(self.centralwidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setGeometry(QRect(220, 270, 61, 61))
        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setGeometry(QRect(220, 340, 61, 61))
        self.pushButton_right = QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setGeometry(QRect(150, 130, 61, 61))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(150, 200, 61, 61))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(150, 270, 61, 61))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 340, 61, 61))
        self.pushButton_ravno = QPushButton(self.centralwidget)
        self.pushButton_ravno.setObjectName(u"pushButton_ravno")
        self.pushButton_ravno.setGeometry(QRect(220, 410, 61, 61))
        self.pushButton_steret = QPushButton(self.centralwidget)
        self.pushButton_steret.setObjectName(u"pushButton_steret")
        self.pushButton_steret.setGeometry(QRect(150, 410, 61, 61))
        self.pushButton_tokha = QPushButton(self.centralwidget)
        self.pushButton_tokha.setObjectName(u"pushButton_tokha")
        self.pushButton_tokha.setGeometry(QRect(80, 410, 61, 61))
        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(10, 410, 61, 61))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 340, 61, 61))
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 340, 61, 61))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 270, 61, 61))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 200, 61, 61))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 270, 61, 61))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(80, 200, 61, 61))
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(10, 130, 61, 61))
        self.pushButton_left = QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setGeometry(QRect(80, 130, 61, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 261, 61))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        #self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"калькулятор", None))
        self.pushButton_del.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_num.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_right.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_ravno.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_steret.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_tokha.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.pushButton_left.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi
