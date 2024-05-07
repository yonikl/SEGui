from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon("image/mainIcon.png"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
