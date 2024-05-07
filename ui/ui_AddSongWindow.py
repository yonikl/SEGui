# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddSong.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_AddSongWindow(object):
    def setupUi(self, AddSongWindow):
        if not AddSongWindow.objectName():
            AddSongWindow.setObjectName(u"AddSongWindow")
        AddSongWindow.resize(284, 233)
        self.centralwidget = QWidget(AddSongWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.song_name_line = QLineEdit(self.centralwidget)
        self.song_name_line.setObjectName(u"song_name_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.song_name_line.sizePolicy().hasHeightForWidth())
        self.song_name_line.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.song_name_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.artist_name_line = QLineEdit(self.centralwidget)
        self.artist_name_line.setObjectName(u"artist_name_line")
        sizePolicy.setHeightForWidth(self.artist_name_line.sizePolicy().hasHeightForWidth())
        self.artist_name_line.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.artist_name_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")

        self.verticalLayout.addWidget(self.submit_button)

        self.message_label = QLabel(self.centralwidget)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setEnabled(True)
        self.message_label.setMaximumSize(QSize(16777215, 20))
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.message_label)

        AddSongWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddSongWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 284, 33))
        AddSongWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddSongWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddSongWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddSongWindow)

        QMetaObject.connectSlotsByName(AddSongWindow)
    # setupUi

    def retranslateUi(self, AddSongWindow):
        AddSongWindow.setWindowTitle(QCoreApplication.translate("AddSongWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddSongWindow", u"Song name:", None))
        self.label_2.setText(QCoreApplication.translate("AddSongWindow", u"Artist name (optional):", None))
        self.submit_button.setText(QCoreApplication.translate("AddSongWindow", u"Add song", None))
        self.message_label.setText("")
    # retranslateUi

