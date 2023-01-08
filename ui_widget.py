# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(640, 480)
        self.horizontalLayout = QHBoxLayout(widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabFeature = QTabWidget(widget)
        self.tabFeature.setObjectName(u"tabFeature")
        self.tabFeature.setStyleSheet(u"")
        self.tab_serial = QWidget()
        self.tab_serial.setObjectName(u"tab_serial")
        self.pushButton = QPushButton(self.tab_serial)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 121, 31))
        self.groupBox = QGroupBox(self.tab_serial)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 70, 181, 261))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 61, 21))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 30, 91, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 61, 21))
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(70, 60, 91, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 61, 21))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 61, 21))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 61, 21))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 180, 61, 21))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 90, 91, 20))
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(70, 120, 68, 22))
        self.comboBox_4 = QComboBox(self.groupBox)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(70, 150, 68, 22))
        self.comboBox_5 = QComboBox(self.groupBox)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(70, 180, 68, 22))
        self.tabFeature.addTab(self.tab_serial, "")
        self.tab_tcp_udp = QWidget()
        self.tab_tcp_udp.setObjectName(u"tab_tcp_udp")
        self.tabFeature.addTab(self.tab_tcp_udp, "")

        self.horizontalLayout.addWidget(self.tabFeature)


        self.retranslateUi(widget)

        self.tabFeature.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u6253\u5f00\u4e32\u53e3", None))
        self.groupBox.setTitle(QCoreApplication.translate("widget", u"\u53c2\u6570\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u6570\u636e\u683c\u5f0f\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("widget", u"RawData", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("widget", u"Format", None))

        self.label_2.setText(QCoreApplication.translate("widget", u"\u7aef\u53e3\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u6ce2\u7279\u7387\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"\u6570\u636e\u4f4d\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("widget", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.tabFeature.setTabText(self.tabFeature.indexOf(self.tab_serial), QCoreApplication.translate("widget", u"Serial", None))
        self.tabFeature.setTabText(self.tabFeature.indexOf(self.tab_tcp_udp), QCoreApplication.translate("widget", u"TCP/UDP", None))
    # retranslateUi

