from typing import TYPE_CHECKING

from PySide6.QtCore import Slot, QDir, Signal, QFile, QIODevice
from PySide6.QtWidgets import QWidget

from .infowindow import InfoWindow

if TYPE_CHECKING:
    from .mainwindow import MainWindow


# MenuWidget class, handle the setup of the Menu of the application
# Handle the changes in the app theme
class MenuWidget(QWidget):
    closing_info_window = Signal()

    def __init__(self, parent: 'MainWindow', change_theme):
        super().__init__()
        self.parent = parent
        self.ui = parent.ui
        self.change_theme = change_theme
        self.info_window = None

        # Setup signals connections
        self.ui.MenuButton.clicked.connect(self.menu_button_clicked)
        self.ui.GoBackButton.clicked.connect(self.go_back_button_clicked)
        self.ui.SettingsButton.clicked.connect(self.settings_button_clicked)
        self.closing_info_window.connect(self.info_window_closed)
        self.ui.InfoButton.clicked.connect(self.info_button_clicked)

        # Setup themes
        parent.settings.beginGroup("Mainwindow")
        self.style_name = parent.settings.value("theme", "default.qss", str)
        self.setup_theme_combo_box(self.style_name)
        self.ui.ThemeComboBox.currentIndexChanged.connect(self.theme_changed)
        parent.settings.endGroup()

    # Add all existing styles to the theme combo box
    def setup_theme_combo_box(self, style_name):
        styles_path = QDir(":/styles/qss")
        index = -1
        for i, file in enumerate(styles_path.entryList()):
            if file == style_name:
                index = i
            self.ui.ThemeComboBox.addItem(file.capitalize().removesuffix(".qss"), file)

        if index == -1:
            style_name = "default.qss"
            index = self.ui.ThemeComboBox.findData(style_name)
        self.ui.ThemeComboBox.setCurrentIndex(index)

        style_path = QFile(":/styles/qss/" + style_name)
        if style_path.open(QIODevice.ReadOnly):
            style = (style_path.readAll()).data().decode("latin1")
            self.change_theme.emit(style)

    @Slot()
    def menu_button_clicked(self):
        self.ui.GoBackButton.hide()
        self.ui.GoBackButton.setEnabled(False)
        if self.ui.LeftBarWidget.isVisible():
            self.ui.LeftBarWidget.hide()
            self.ui.LeftBarStackedWidget.setCurrentWidget(self.ui.MenuBarPage)
        else:
            self.ui.LeftBarWidget.show()

    @Slot(int)
    def theme_changed(self, _):
        selected_data = self.ui.ThemeComboBox.currentData()

        self.style_name = selected_data
        self.parent.settings.beginGroup("Mainwindow")
        self.parent.settings.setValue("theme", selected_data)
        self.parent.settings.endGroup()

        style_path = QFile(":/styles/qss/" + selected_data)
        if style_path.open(QIODevice.ReadOnly):
            style = (style_path.readAll()).data().decode("latin1")
            self.change_theme.emit(style)

    @Slot()
    def go_back_button_clicked(self):
        self.ui.LeftBarStackedWidget.setCurrentWidget(self.ui.MenuBarPage)

    @Slot()
    def settings_button_clicked(self):
        self.ui.GoBackButton.setEnabled(True)
        self.ui.LeftBarStackedWidget.setCurrentWidget(self.ui.SettingsPage)
        self.ui.GoBackButton.show()

    @Slot()
    def info_button_clicked(self):
        if self.info_window is None:
            self.info_window = InfoWindow(self.style_name, self.closing_info_window, self.change_theme)

    @Slot()
    def info_window_closed(self):
        self.info_window = None
