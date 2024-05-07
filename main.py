import sys
from PySide6.QtWidgets import QApplication
from presenter.Presenter import Presenter
from view.MainWindowView import MainWindow
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    Presenter(window)
    window.show()
    apply_stylesheet(app, theme='dark_teal.xml')

    sys.exit(app.exec())