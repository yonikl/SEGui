# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SongWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 100)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ImageLabel = QLabel(Form)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ImageLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TrackNameLabel = QLabel(Form)
        self.TrackNameLabel.setObjectName(u"TrackNameLabel")

        self.verticalLayout.addWidget(self.TrackNameLabel)

        self.ArtistNameLabel = QLabel(Form)
        self.ArtistNameLabel.setObjectName(u"ArtistNameLabel")

        self.verticalLayout.addWidget(self.ArtistNameLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ImageLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.TrackNameLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.ArtistNameLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

