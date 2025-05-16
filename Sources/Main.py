import sys
import os
import glob
from datetime import datetime
import configparser
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from Logic.operation_handler import is_valid_en, is_valid_serial

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:\Projects\Dispensing_Machines\Sources\GUI\dispensing_machine_main.ui", self)

        self.MC = os.environ['COMPUTERNAME']

        self.MainstackedWidget.setCurrentIndex(0)
        self.enLineEdit.setFocus()
        self.LoginButton.clicked.connect(self.check_login)
        self.LogoutButton.clicked.connect(self.logout)
        self.StartButton.clicked.connect(self.check_main)
        self.FinishButton.clicked.connect(self.final_process)

    def check_login(self):
        self.en = self.enLineEdit.text()
        if is_valid_en(self.en):
            self.Operation = self.comboBoxOperation.currentText()
            QTimer.singleShot(100, self.mainWindow)
        else:
            self.label_Error_login.setText("Incorrect EN.")
            self.label_Error_login.setStyleSheet("color: red;")

    def mainWindow(self):
        print("Step Main")
        self.MainstackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_Serial.setFocus()
        self.LogoutButton.show()
        self.lineEdit_Operator.setText(self.en)
        self.lineEdit_Operation.setText(self.Operation)
        self.lineEdit_Station.setText(self.MC)

    def logout(self):
        print("Step Logout")
        self.enLineEdit.setFocus()
        self.MainstackedWidget.setCurrentIndex(0)

    def check_main(self):
        self.Serial = self.lineEdit_Serial.text()
        self.epoxy = self.EPOXY_Value.text()
        if not is_valid_serial(self.Serial):
            self.label_Error_Main.setText("Please check Serial Number.")
            self.label_Error_Main.setStyleSheet("color: red;")
        elif not self.epoxy:
            self.label_Error_Main.setText("Please check EPOXY ID.")
            self.label_Error_Main.setStyleSheet("color: red;")           
        else:
            self.LogoutButton.hide()
            QTimer.singleShot(100, self.mainprocess)

    def mainprocess(self):
        print("Step Start")
        self.stackedWidget.setCurrentIndex(1)
        self.FinishButton.hide()
        # Check status of Nordson by I/O signal

        # sent 3 Output via digitial I/O box modbus "Call Program" into Nordson machine

        # sent 1 Output via digitial I/O box modbus "Start" into Nordson machine  

        # Nordson sent Status via digitial I/O box modbus

        # wait until Nordson sent result via digitial I/O box modbus 

        # When finish process and recive result pass/fail from I/O set FinishButton to show() 

    def final_process(self):
        print("Step Result")
        # create log file and upload data result into database


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.showMaximized()
    sys.exit(app.exec())        