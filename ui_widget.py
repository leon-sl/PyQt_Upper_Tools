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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTextBrowser, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(664, 446)
        self.horizontalLayout = QHBoxLayout(widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabFeature = QTabWidget(widget)
        self.tabFeature.setObjectName(u"tabFeature")
        self.tabFeature.setStyleSheet(u"")
        self.tab_serial = QWidget()
        self.tab_serial.setObjectName(u"tab_serial")
        self.push_button_open_serial = QPushButton(self.tab_serial)
        self.push_button_open_serial.setObjectName(u"push_button_open_serial")
        self.push_button_open_serial.setGeometry(QRect(20, 20, 121, 31))
        self.group_box_setting = QGroupBox(self.tab_serial)
        self.group_box_setting.setObjectName(u"group_box_setting")
        self.group_box_setting.setGeometry(QRect(20, 70, 181, 221))
        self.label_format = QLabel(self.group_box_setting)
        self.label_format.setObjectName(u"label_format")
        self.label_format.setGeometry(QRect(10, 30, 61, 21))
        self.combo_box_format = QComboBox(self.group_box_setting)
        self.combo_box_format.addItem("")
        self.combo_box_format.addItem("")
        self.combo_box_format.setObjectName(u"combo_box_format")
        self.combo_box_format.setGeometry(QRect(70, 30, 91, 22))
        self.label_serial_index = QLabel(self.group_box_setting)
        self.label_serial_index.setObjectName(u"label_serial_index")
        self.label_serial_index.setGeometry(QRect(10, 60, 61, 21))
        self.combo_box_serial_index = QComboBox(self.group_box_setting)
        self.combo_box_serial_index.addItem("")
        self.combo_box_serial_index.setObjectName(u"combo_box_serial_index")
        self.combo_box_serial_index.setGeometry(QRect(70, 60, 91, 22))
        self.label_baudrate = QLabel(self.group_box_setting)
        self.label_baudrate.setObjectName(u"label_baudrate")
        self.label_baudrate.setGeometry(QRect(10, 90, 61, 21))
        self.label_data_bit = QLabel(self.group_box_setting)
        self.label_data_bit.setObjectName(u"label_data_bit")
        self.label_data_bit.setGeometry(QRect(10, 120, 61, 21))
        self.label_parity_bit = QLabel(self.group_box_setting)
        self.label_parity_bit.setObjectName(u"label_parity_bit")
        self.label_parity_bit.setGeometry(QRect(10, 150, 61, 21))
        self.label_stop_bit = QLabel(self.group_box_setting)
        self.label_stop_bit.setObjectName(u"label_stop_bit")
        self.label_stop_bit.setGeometry(QRect(10, 180, 61, 21))
        self.line_edit_baudrate = QLineEdit(self.group_box_setting)
        self.line_edit_baudrate.setObjectName(u"line_edit_baudrate")
        self.line_edit_baudrate.setGeometry(QRect(70, 90, 91, 20))
        self.combo_box_data_bit = QComboBox(self.group_box_setting)
        self.combo_box_data_bit.setObjectName(u"combo_box_data_bit")
        self.combo_box_data_bit.setGeometry(QRect(70, 120, 68, 22))
        self.combo_box_parity_bit = QComboBox(self.group_box_setting)
        self.combo_box_parity_bit.setObjectName(u"combo_box_parity_bit")
        self.combo_box_parity_bit.setGeometry(QRect(70, 150, 68, 22))
        self.combo_box_stop_bit = QComboBox(self.group_box_setting)
        self.combo_box_stop_bit.setObjectName(u"combo_box_stop_bit")
        self.combo_box_stop_bit.setGeometry(QRect(70, 180, 68, 22))
        self.label_rx_space = QLabel(self.tab_serial)
        self.label_rx_space.setObjectName(u"label_rx_space")
        self.label_rx_space.setGeometry(QRect(210, 20, 54, 16))
        self.text_browser_rx_space = QTextBrowser(self.tab_serial)
        self.text_browser_rx_space.setObjectName(u"text_browser_rx_space")
        self.text_browser_rx_space.setGeometry(QRect(210, 40, 391, 181))
        self.label_tx_space = QLabel(self.tab_serial)
        self.label_tx_space.setObjectName(u"label_tx_space")
        self.label_tx_space.setGeometry(QRect(210, 260, 54, 16))
        self.text_browser_tx_space = QTextBrowser(self.tab_serial)
        self.text_browser_tx_space.setObjectName(u"text_browser_tx_space")
        self.text_browser_tx_space.setGeometry(QRect(210, 280, 391, 61))
        self.pushButton_start_send = QPushButton(self.tab_serial)
        self.pushButton_start_send.setObjectName(u"pushButton_start_send")
        self.pushButton_start_send.setGeometry(QRect(530, 350, 75, 24))
        self.check_box_tx_hex_2 = QCheckBox(self.tab_serial)
        self.check_box_tx_hex_2.setObjectName(u"check_box_tx_hex_2")
        self.check_box_tx_hex_2.setGeometry(QRect(210, 350, 51, 20))
        self.check_box_tx_hex_2.setAutoExclusive(True)
        self.check_box_tx_str = QCheckBox(self.tab_serial)
        self.check_box_tx_str.setObjectName(u"check_box_tx_str")
        self.check_box_tx_str.setGeometry(QRect(260, 350, 61, 20))
        self.check_box_tx_str.setAutoExclusive(True)
        self.combo_box_tx_append = QComboBox(self.tab_serial)
        self.combo_box_tx_append.addItem("")
        self.combo_box_tx_append.addItem("")
        self.combo_box_tx_append.addItem("")
        self.combo_box_tx_append.addItem("")
        self.combo_box_tx_append.setObjectName(u"combo_box_tx_append")
        self.combo_box_tx_append.setGeometry(QRect(330, 350, 68, 22))
        self.label_timer = QLabel(self.tab_serial)
        self.label_timer.setObjectName(u"label_timer")
        self.label_timer.setGeometry(QRect(400, 350, 31, 16))
        self.line_edit_timer = QLineEdit(self.tab_serial)
        self.line_edit_timer.setObjectName(u"line_edit_timer")
        self.line_edit_timer.setGeometry(QRect(430, 350, 61, 20))
        self.label_timer_ms = QLabel(self.tab_serial)
        self.label_timer_ms.setObjectName(u"label_timer_ms")
        self.label_timer_ms.setGeometry(QRect(500, 350, 21, 16))
        self.check_box_time_stamp = QCheckBox(self.tab_serial)
        self.check_box_time_stamp.setObjectName(u"check_box_time_stamp")
        self.check_box_time_stamp.setGeometry(QRect(470, 230, 61, 20))
        self.push_button_rx_clear = QPushButton(self.tab_serial)
        self.push_button_rx_clear.setObjectName(u"push_button_rx_clear")
        self.push_button_rx_clear.setGeometry(QRect(530, 230, 71, 24))
        self.check_box_rx_str = QCheckBox(self.tab_serial)
        self.check_box_rx_str.setObjectName(u"check_box_rx_str")
        self.check_box_rx_str.setGeometry(QRect(410, 230, 61, 20))
        self.check_box_rx_str.setAutoExclusive(False)
        self.check_box_tx_hex = QCheckBox(self.tab_serial)
        self.check_box_tx_hex.setObjectName(u"check_box_tx_hex")
        self.check_box_tx_hex.setGeometry(QRect(360, 230, 51, 20))
        self.group_box_tx_rx_count = QGroupBox(self.tab_serial)
        self.group_box_tx_rx_count.setObjectName(u"group_box_tx_rx_count")
        self.group_box_tx_rx_count.setGeometry(QRect(20, 290, 120, 80))
        self.label_tx_count = QLabel(self.group_box_tx_rx_count)
        self.label_tx_count.setObjectName(u"label_tx_count")
        self.label_tx_count.setGeometry(QRect(10, 20, 31, 16))
        self.line_edit_tx_count = QLineEdit(self.group_box_tx_rx_count)
        self.line_edit_tx_count.setObjectName(u"line_edit_tx_count")
        self.line_edit_tx_count.setGeometry(QRect(30, 20, 61, 20))
        self.label_rx_count = QLabel(self.group_box_tx_rx_count)
        self.label_rx_count.setObjectName(u"label_rx_count")
        self.label_rx_count.setGeometry(QRect(10, 50, 31, 16))
        self.line_edit_rx_count = QLineEdit(self.group_box_tx_rx_count)
        self.line_edit_rx_count.setObjectName(u"line_edit_rx_count")
        self.line_edit_rx_count.setGeometry(QRect(30, 50, 61, 20))
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
        self.push_button_open_serial.setText(QCoreApplication.translate("widget", u"\u6253\u5f00\u4e32\u53e3", None))
        self.group_box_setting.setTitle(QCoreApplication.translate("widget", u"\u53c2\u6570\u914d\u7f6e", None))
        self.label_format.setText(QCoreApplication.translate("widget", u"\u6570\u636e\u683c\u5f0f\uff1a", None))
        self.combo_box_format.setItemText(0, QCoreApplication.translate("widget", u"RawData", None))
        self.combo_box_format.setItemText(1, QCoreApplication.translate("widget", u"Format", None))

        self.label_serial_index.setText(QCoreApplication.translate("widget", u"\u7aef\u53e3\u53f7\uff1a", None))
        self.combo_box_serial_index.setItemText(0, "")

        self.label_baudrate.setText(QCoreApplication.translate("widget", u"\u6ce2\u7279\u7387\uff1a", None))
        self.label_data_bit.setText(QCoreApplication.translate("widget", u"\u6570\u636e\u4f4d\uff1a", None))
        self.label_parity_bit.setText(QCoreApplication.translate("widget", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.label_stop_bit.setText(QCoreApplication.translate("widget", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.label_rx_space.setText(QCoreApplication.translate("widget", u"\u63a5\u6536\u533a\uff1a", None))
        self.label_tx_space.setText(QCoreApplication.translate("widget", u"\u53d1\u9001\u533a\uff1a", None))
        self.text_browser_tx_space.setHtml(QCoreApplication.translate("widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12345</p></body></html>", None))
        self.pushButton_start_send.setText(QCoreApplication.translate("widget", u"\u5f00\u59cb\u53d1\u9001", None))
        self.check_box_tx_hex_2.setText(QCoreApplication.translate("widget", u"Hex", None))
        self.check_box_tx_str.setText(QCoreApplication.translate("widget", u"\u5b57\u7b26\u4e32", None))
        self.combo_box_tx_append.setItemText(0, QCoreApplication.translate("widget", u"None", None))
        self.combo_box_tx_append.setItemText(1, QCoreApplication.translate("widget", u"\\r", None))
        self.combo_box_tx_append.setItemText(2, QCoreApplication.translate("widget", u"\\n", None))
        self.combo_box_tx_append.setItemText(3, QCoreApplication.translate("widget", u"\\r\\n", None))

        self.label_timer.setText(QCoreApplication.translate("widget", u"\u5b9a\u65f6\uff1a", None))
        self.label_timer_ms.setText(QCoreApplication.translate("widget", u"ms", None))
        self.check_box_time_stamp.setText(QCoreApplication.translate("widget", u"\u65f6\u95f4\u6233", None))
        self.push_button_rx_clear.setText(QCoreApplication.translate("widget", u"\u6e05\u7a7a", None))
        self.check_box_rx_str.setText(QCoreApplication.translate("widget", u"\u5b57\u7b26\u4e32", None))
        self.check_box_tx_hex.setText(QCoreApplication.translate("widget", u"Hex", None))
        self.group_box_tx_rx_count.setTitle(QCoreApplication.translate("widget", u"\u6536\u53d1\u8ba1\u6570", None))
        self.label_tx_count.setText(QCoreApplication.translate("widget", u"TX", None))
        self.label_rx_count.setText(QCoreApplication.translate("widget", u"RX", None))
        self.tabFeature.setTabText(self.tabFeature.indexOf(self.tab_serial), QCoreApplication.translate("widget", u"Serial", None))
        self.tabFeature.setTabText(self.tabFeature.indexOf(self.tab_tcp_udp), QCoreApplication.translate("widget", u"TCP/UDP", None))
    # retranslateUi

