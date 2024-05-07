from PySide6.QtWidgets import QMainWindow
from ui.ui_AddSongWindow import Ui_AddSongWindow


class AddSongWindow(QMainWindow):
    def __init__(self):
        super(AddSongWindow, self).__init__()
        self.setWindowTitle("Add New Song")
        self.ui = Ui_AddSongWindow()
        self.ui.setupUi(self)
