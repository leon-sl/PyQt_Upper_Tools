from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo 
from PySide6.QtCore import QTimer
# from ui_widget import Ui_widget

SCAN_COM_TIMER_MS = 2000
BLANK_STRING = "N/A"
CLOSE_STRING = "CLOSED"
OPEN_STRING = "OPEN"

class Setting():

    def __init__(self):
        self.str_com_name = ""      #COM4
        self.str_data_format = ""
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
        self.serial_status = CLOSE_STRING
        self.current_setting = Setting()
        self.serial = QSerialPort()

        self.ui.push_button_scan_serial.clicked.connect(self.scan_serial_port)
        self.ui.push_button_open_serial.clicked.connect(self.open_close_serial_port)
        self.serial.readyRead.connect(self.read_data)
        # self.ui.combo_box_serial_index.textActivated.connect(self.widget_test)

    @Slot()
    def scan_serial_port(self):
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

    def setting_prebuilt_and_update(self):
        setting_dic = {
            "None": QSerialPort.Parity.NoParity,
            "Even": QSerialPort.Parity.EvenParity,
            "Odd":  QSerialPort.Parity.OddParity,

            "8":    QSerialPort.DataBits.Data8,
            "7":    QSerialPort.DataBits.Data7,
            "6":    QSerialPort.DataBits.Data6,

            "1":    QSerialPort.StopBits.OneStop,
            "2":    QSerialPort.StopBits.TwoStop
        }

        self.current_setting.str_com_name = self.ui.combo_box_serial_index.currentText()
        self.current_setting.str_baud_rate = self.ui.line_edit_baudrate.text()
        self.current_setting.baud_rate = int(self.current_setting.str_baud_rate)
        self.current_setting.str_data_bits = self.ui.combo_box_data_bit.currentText()
        self.current_setting.data_bits = setting_dic[self.current_setting.str_data_bits]

        self.current_setting.str_stop_bits = self.ui.combo_box_stop_bit.currentText()
        self.current_setting.stop_bits = setting_dic[self.current_setting.str_stop_bits]

        self.current_setting.str_parity_bits = self.ui.combo_box_parity_bit.currentText()
        self.current_setting.parity_bits = setting_dic[self.current_setting.str_parity_bits]

        self.current_setting.str_data_format = self.ui.combo_box_format.currentText()

        # print(self.current_setting.baud_rate, self.current_setting.data_bits, self.current_setting.stop_bits, self.current_setting.parity_bits)

    @Slot()
    def open_close_serial_port(self):
        self.setting_prebuilt_and_update()

        self.serial.setPortName(self.current_setting.str_com_name)
        self.serial.setBaudRate(self.current_setting.baud_rate)
        self.serial.setDataBits(self.current_setting.data_bits)
        self.serial.setParity(self.current_setting.parity_bits)
        self.serial.setStopBits(self.current_setting.stop_bits)
        self.serial.setFlowControl(self.current_setting.flow_control)

        if self.serial_status == CLOSE_STRING:
            if self.serial.open(QIODeviceBase.ReadWrite):
                self.ui.push_button_open_serial.setText("关闭串口")
                self.serial_status = OPEN_STRING
                print(self.current_setting.str_com_name + "open success!")
            else:
                print(self.current_setting.str_com_name + "open failed!")
        elif self.serial_status == OPEN_STRING:
            self.serial.close()
            self.ui.push_button_open_serial.setText("打开串口")
            print(self.current_setting.str_com_name + "closed!")

    @Slot()
    def read_data(self):
        data = self.serial.readAll()
        print(data)

    @Slot()
    def widget_test(self):
        print("\nupdate setting:")
        print("combo_box_serial_index current text:", self.ui.combo_box_serial_index.currentText())
        print("combo_box_format current text:", self.ui.combo_box_format.currentText())
        print("combo_box_data_bit current text:", self.ui.combo_box_data_bit.currentText())
        print("combo_box_parity_bit current text:", self.ui.combo_box_parity_bit.currentText())
        print("combo_box_stop_bit current text:", self.ui.combo_box_stop_bit.currentText())
        print("line_edit_baudrate current text:", self.ui.line_edit_baudrate.text())