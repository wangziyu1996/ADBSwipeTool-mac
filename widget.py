from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QWidget
from swipetool_ui import Ui_Widget
import threading
import time
import subprocess

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adb_path = "platform-tools-mac/adb"
        self.setWindowTitle("ADB Swipe Tool")
        self.load_combobox_items()
        self.start_x_axis_lineedit.setText("500")
        self.start_y_axis_lineedit.setText("500")
        self.end_x_axis_lineedit.setText("500")
        self.end_y_axis_lineedit.setText("800")
        self.pause_duration_spinbox.setValue(3)
        self.start_button.setShortcut(QKeySequence(Qt.Key_Return))
        self.start_button.clicked.connect(self.a)
        self.stop_button.setShortcut(QKeySequence(Qt.Key_Escape))
        self.stop_button.clicked.connect(self.stop_swipe)


    def load_combobox_items(self):
        subprocess.getoutput(f"{self.adb_path} kill-server")
        subprocess.getoutput(f"{self.adb_path} start-server")
        adb_output = subprocess.getoutput(f"{self.adb_path} devices")
        devices = adb_output.strip().split("\n")[1:]  # Remove the header and split into lines
        device_list = [device.split("\t")[0] for device in devices if "\tdevice" in device]
        self.comboBox.addItems(device_list)
        
    def a(self):
        t = threading.Thread(target = self.swipe_action, name='t')
        t.start()

    def swipe_action(self):
        self.flag = 1
        #self.lockwidgets()
        selected_device = self.comboBox.currentText()
        startXAxis = int(self.start_x_axis_lineedit.text())
        startYAxis = int(self.start_y_axis_lineedit.text())
        endXAxis = int(self.end_x_axis_lineedit.text())
        endYAxis = int(self.end_y_axis_lineedit.text())
        duration = 500
        pause_duration = int(self.pause_duration_spinbox.value())
        loop_times = self.swipe_times_spinbox.value()

        for times in range(loop_times):
            subprocess.getoutput(f"{self.adb_path} -s {selected_device} shell input swipe {startXAxis} {startYAxis} {endXAxis} {endYAxis} {duration}")
            time.sleep(pause_duration)
            if self.flag == 0:
                #self.unlockwidgets()
                return
            
    def stop_swipe(self):
        self.flag = 0

"""   
    def lockwidgets(self):
        self.comboBox.setEnabled(False)
        self.start_x_axis_lineedit.setEnabled(False)
        self.start_y_axis_lineedit.setEnabled(False)
        self.end_x_axis_lineedit.setEnabled(False)
        self.end_y_axis_lineedit.setEnabled(False)
        self.pause_duration_spinbox.setEnabled(False)
        self.swipe_times_spinbox.setEnabled(False)

    def unlockwidgets(self):
        self.comboBox.setEnabled(True)
        self.start_x_axis_lineedit.setEnabled(True)
        self.start_y_axis_lineedit.setEnabled(True)
        self.end_x_axis_lineedit.setEnabled(True)
        self.end_y_axis_lineedit.setEnabled(True)
        self.pause_duration_spinbox.setEnabled(True)
        self.swipe_times_spinbox.setEnabled(True)
"""




        
        
        
