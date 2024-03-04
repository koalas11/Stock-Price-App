import os

from PySide6.QtCore import Slot, QFile, QIODevice
from PySide6.QtWidgets import QWidget

from ..Constants import APP_ICON, CONFIG_PATH
from .generated.ui_infowindow import Ui_InfoForm


# InfoWindow class, opens the info window
class InfoWindow(QWidget):

    def __init__(self, style_name, closing_window, theme_changed):
        super().__init__()
        self.closing_window = closing_window
        theme_changed.connect(self.theme_changed)
        self.ui = Ui_InfoForm()
        self.ui.setupUi(self)
        self.setLayout(self.ui.MainLayout)
        self.setWindowIcon(APP_ICON)
        self.set_theme(style_name)
        self.ui.ConfigValue.setText(str(os.path.normpath(CONFIG_PATH)))

        # Set fixed size
        self.repaint()
        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())
        self.show()

    def set_theme(self, style_name):
        style_path = QFile(":/styles/qss/" + style_name)
        if style_path.open(QIODevice.ReadOnly):
            self.ui.MainWidget.setStyleSheet((style_path.readAll()).data().decode("latin1"))

    @Slot(str)
    def theme_changed(self, style_name):
        self.set_theme(style_name)

    def closeEvent(self, event):
        self.closing_window.emit()
        super().closeEvent(event)
