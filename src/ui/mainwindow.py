from PySide6.QtCore import Signal, Slot, QSettings
from PySide6.QtWidgets import QMainWindow, QApplication
from pandas import DataFrame

from ..stock_price import WorkerThread
from .generated.ui_mainwindow import Ui_MainWindow
from .maincontainer import MainContainer
from .menuwidget import MenuWidget
from .tickerbox import TickerBox


# MainWindow class, handle the setup of the main window
# Connects all signal to the designated slots
# Set up the widget associated with the main window
class MainWindow(QMainWindow):
    update_chart = Signal(DataFrame)
    loading_end = Signal(bool)
    change_theme = Signal(str)
    ticker_changed = Signal()
    app_closing = Signal()
    finish_signal = Signal()

    def __init__(self, app: QApplication, settings: QSettings):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.app = app
        self.settings = settings
        self.ui.setupUi(self)

        # Set up Main Container (the chart Widget)
        self.main_container = MainContainer(self)

        self.loading_end.connect(self.main_container.show_chart)
        self.ticker_changed.connect(self.main_container.hide_chart)
        self.update_chart[DataFrame].connect(self.main_container.chart.update_chart)

        # Set up the thread for background work and the ticker group box
        self.thread = WorkerThread(self.finish_signal, self.update_chart, self.loading_end)
        self.ticker = TickerBox(self, self.thread, self.ticker_changed)
        self.finish_signal.connect(self.ticker.start_background_work)
        self.app_closing.connect(self.thread.stop)

        # Setup Menu and Theme
        self.change_theme.connect(self.theme_changed)
        self.change_theme.connect(self.main_container.theme_changed)
        self.change_theme.connect(self.main_container.chart.theme_changed)

        self.menu = MenuWidget(self, self.change_theme)
        self.ui.LeftBarWidget.hide()

    @Slot(str)
    def theme_changed(self, style):
        self.app.setStyleSheet(style)

    def closeEvent(self, event):
        self.app_closing.emit()
        settings = self.settings
        settings.beginGroup("Mainwindow")
        settings.setValue("size", self.size())
        settings.setValue("maximized", self.isMaximized())
        settings.endGroup()

        if self.menu.info_window is not None:
            self.menu.info_window.close()

        super().closeEvent(event)
