from urllib.request import urlopen

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QListWidgetItem, QMenu

from model.SongModel import SongsModel
from view.MainWindowView import MainWindow
from view.SongWidgetView import SongWidgetView
from view.AddSongWindowView import AddSongWindow
from view.UpdateSongView import UpdateSongView
from PySide6.QtGui import QIcon

class Presenter:
    def __init__(self, view: MainWindow):
        self.song_view = None
        self.add_song_window = None
        self.view = view
        self.Model = SongsModel()
        self.Songs = None
        self.view.ui.search_button.clicked.connect(self.search)
        self.view.ui.AddSongButton.clicked.connect(self.open_add_song)
        self.populate_view()

    def show_context_menu(self, event, sender):
        menu = QMenu(self.view)

        update_action = menu.addAction("Update")
        delete_action = menu.addAction("Delete")

        global_pos = QCursor.pos()

        action = menu.exec_(global_pos)

        if action == update_action:
            self.update_song(sender)
        elif action == delete_action:
            self.delete_song(sender.id)

    def populate_view(self, search=None):
        self.Songs = self.Model.get_songs(search)
        self.view.ui.SongList.clear()
        for song in self.Songs:
            item = QListWidgetItem()
            song_widget = SongWidgetView(self.image_processing(song['imagePath']), song['name'], song['artistName'],
                                         song['id'])
            song_widget.setContextMenuPolicy(Qt.CustomContextMenu)
            song_widget.customContextMenuRequested.connect(
                lambda event, label=song_widget: self.show_context_menu(event, label))
            song_widget.mousePressEvent = lambda event, sender=song_widget: self.show_song_details(event, sender)
            item.setSizeHint(song_widget.sizeHint())
            self.view.ui.SongList.addItem(item)
            self.view.ui.SongList.setItemWidget(item, song_widget)

    def delete_song(self, id):
        self.Model.delete_song(id)
        self.populate_view()

    def open_add_song(self):
        self.add_song_window = AddSongWindow()
        self.add_song_window.ui.submit_button.clicked.connect(self.add_song)
        self.add_song_window.setWindowIcon(QIcon("image/mainIcon.png"))
        self.add_song_window.show()

    def add_song(self):
        song_name = self.add_song_window.ui.song_name_line.text()
        artist_name = self.add_song_window.ui.artist_name_line.text()
        self.add_song_window.ui.message_label.setText(
            self.Model.add_song({"trackName": f"{song_name}", "artistName": f"{artist_name}"}))
        self.populate_view()

    def show_song_details(self, event, sender):
        if event.button() == Qt.LeftButton:
            self.update_song(sender)
            self.song_view.setWindowTitle("Song details")
            self.song_view.ui.update_button.hide()
            self.song_view.ui.song_name.setReadOnly(True)
            self.song_view.ui.artist_name.setReadOnly(True)

    def update_song(self, sender):
        self.song_view = UpdateSongView()
        song = [i for i in self.Songs if i['id'] == sender.id][0]
        image = self.image_processing(song['imagePath'])
        self.song_view.setWindowIcon(QIcon(image))
        self.song_view.ui.image.setPixmap(image)
        self.song_view.ui.song_name.setText(song['name'])
        self.song_view.ui.artist_name.setText(song['artistName'])
        self.song_view.ui.lyrics.setText(song['lyrics'])
        self.song_view.ui.update_button.clicked.connect(lambda: self.update_song_in_model(song))
        self.song_view.show()

    def search(self):
        search = self.view.ui.SearchLine.text()
        self.populate_view(search)

    def image_processing(self, path):
        url_data = urlopen(path).read()
        pixmap = QPixmap()
        pixmap.loadFromData(url_data)
        return pixmap

    def update_song_in_model(self, song):
        self.Model.update_song(song['id'], {"name": self.song_view.ui.song_name.text(),
                                            "artistName": self.song_view.ui.artist_name.text(),
                                            "id": song['id']})
        self.populate_view()
