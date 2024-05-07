from PySide6.QtWidgets import QMainWindow
from ui.ui_UpdateSongWindow import Ui_MainWindow


class UpdateSongView(QMainWindow):
    def __init__(self):
        super(UpdateSongView, self).__init__()
        self.setWindowTitle("Update Song")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)