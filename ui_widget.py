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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QTabWidget,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(640, 480)
        self.horizontalLayout = QHBoxLayout(widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabFeature = QTabWidget(widget)
        self.tabFeature.setObjectName(u"tabFeature")
        self.tab_serial = QWidget()
        self.tab_serial.setObjectName(u"tab_serial")
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
        self.tabFeature.setTabText(self.tabFeature.indexOf(self.tab_serial), QCoreApplication.translate("widget", u"Serial", None))
        self.tabFeature.setTabText(self.tabFeature.indexOf(self.tab_tcp_udp), QCoreApplication.translate("widget", u"TCP/UDP", None))
    # retranslateUi

