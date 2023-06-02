from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QpushButton, QLabel, QVBoxLayout
from instr import*
from second_win import*


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        pass
    def initUI(self):
        pass
    def connects(self):
        pass
