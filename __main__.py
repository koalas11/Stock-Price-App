import sys

from PySide6.QtCore import QSettings, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from src.Constants import CONFIG_FILE, APP_ICON
from src.ui.mainwindow import MainWindow

# Start file of the application
# Set up the main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    APP_ICON.addFile(":/icons/icons/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)

    settings = QSettings(CONFIG_FILE, QSettings.IniFormat)
    window = MainWindow(app, settings)

    settings.beginGroup("Mainwindow")
    if settings.value("maximized", False, bool):
        window.showMaximized()
    else:
        size = settings.value("size", window.size(), QSize)
        window.resize(size)
        window.show()
    settings.endGroup()

    sys.exit(app.exec())
