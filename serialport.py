from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo 
from PySide6.QtCore import QTimer
# from ui_widget import Ui_widget

SCAN_COM_TIMER_MS = 2000
BLANK_STRING = "N/A"

class Setting():

    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.str_baud_rate = ""
        self.data_bits = QSerialPort.DataBits.Data8
        self.str_data_bits = ""
        self.stop_bits = QSerialPort.StopBits.OneStop
        self.str_stop_bits = ""
        self.parity_bits = QSerialPort.Parity.NoParity
        self.str_parity_bits = ""
        self.flow_control = QSerialPort.FlowControl.NoFlowControl

class SerialPort():

    def __init__(self, ui):

        # self.ui = Ui_widget(ui)
        self.ui = ui
        self.current_setting = Setting()
        # self.timer_scan_com = QTimer()
        # self.timer_scan_com.timeout.connect(self.show_port_info)
        # self.timer_scan_com.start(SCAN_COM_TIMER_MS)
        
        self.ui.push_button_scan_serial.clicked.connect(self.scan_port)
        self.ui.combo_box_serial_index.textActivated.connect(self.widget_test)

    def scan_port(self):
        self.ui.combo_box_serial_index.clear()
        for info in QSerialPortInfo.availablePorts():
            list = []
            description = info.description()
            manufacturer = info.manufacturer()
            serial_number = info.serialNumber()
            list.append(info.portName())
            list.append(description if description else BLANK_STRING)
            list.append(manufacturer if manufacturer else BLANK_STRING)
            list.append(serial_number if serial_number else BLANK_STRING)
            list.append(info.systemLocation())
            vid = info.vendorIdentifier()
            list.append(f"{vid:x}" if vid else BLANK_STRING)
            pid = info.productIdentifier()
            list.append(f"{pid:x}" if pid else BLANK_STRING)
            self.ui.combo_box_serial_index.addItem(list[0], list)

    def widget_test(self):
        print("current index:", self.ui.combo_box_serial_index.currentIndex())