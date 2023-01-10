from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo 
from PySide6.QtCore import QTimer
from ui_widget import Ui_widget

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
        self.current_setting = Setting()
        self.timer_scan_com = QTimer()
        self.timer_scan_com.timeout.connect(self.show_port_info)
        self.timer_scan_com.start(SCAN_COM_TIMER_MS)
        # self.ui = Ui_widget()

        # ui.combo_box_serial_index.activated.connect(self.show_port_info)
    
    def scan_port(self):
        pass


    def show_port_info(self):
        list = []
        for info in QSerialPortInfo.availablePorts():
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

        print(list)
        self.timer_scan_com.start(SCAN_COM_TIMER_MS)