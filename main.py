import time
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QHeaderView,
                             QMainWindow, QMessageBox, QTableWidgetItem,QMenu,QAction,QFileDialog)

from prompt import prompt

class PROMPT(QThread):
    PromptOutPut = pyqtSignal(str)
    def __init__(self, parent=None):
        super(PROMPT, self).__init__(parent)
        self.connecting = True

    def __del__(self):
        self.connceting = False
        # self.wait()
    def run(self):
        while True:
            time.sleep(10)
            self.PromptOutPut.emit(prompt())

class Monitor(QThread):
    MonitorOutPut = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Monitor, self).__init__(parent)
        self.connecting = True

    def __del__(self):
        self.connceting = False
        # self.wait()
    def run(self):
        pass
class Minecraft:
    def __init__(self,parent=None):
        self.ui = uic.loadUi('QTUI/main.ui')
        #self.ui.setWindowIcon(QIcon('MCPEManager.ico'))


        self.Promot_QThread = PROMPT()
        self.Promot_QThread.PromptOutPut.connect(self.PromptLabel)
        self.Promot_QThread.start()
    
    def PromptLabel(self,prompt_str):
        self.ui.prompt.setText(prompt_str)


if __name__ == '__main__':
    add = QApplication([])
    minecraft = Minecraft()
    minecraft.ui.show()
    add.exec_()