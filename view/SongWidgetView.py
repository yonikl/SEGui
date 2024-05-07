from PySide6.QtWidgets import QWidget
from ui.ui_SongWidget import Ui_Form


class SongWidgetView(QWidget):
    def __init__(self, Image, TrackName, ArtistName, id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id = id
        self.ui.ImageLabel.setPixmap(Image)
        self.ui.TrackNameLabel.setText(TrackName)
        self.ui.ArtistNameLabel.setText(ArtistName)


