from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ..stock_price import WorkerThread

if TYPE_CHECKING:
    from .mainwindow import MainWindow


# TickerBox class, handle the setup of the Ticker box
class TickerBox(QWidget):
    intervals = (
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
    )

    periods = (
        "1d",
        "2d",
        "3d",
        "4d",
        "5d",
        "6d",
        "7d",
    )

    def __init__(self, main_window: 'MainWindow', thread: WorkerThread, ticker_changed):
        super().__init__()
        self.main_window = main_window
        self.thread = thread
        self.ticker_changed = ticker_changed

        # Set up Ticker Box Values
        main_window.settings.beginGroup("Ticker")
        ticker = main_window.settings.value("ticker", "META", str)
        interval = main_window.settings.value("interval", "1m", str)
        period = main_window.settings.value("period", "1d", str)
        main_window.settings.endGroup()

        try:
            self.interval_index = self.intervals.index(interval)
            self.period_index = self.periods.index(period)
        except ValueError:
            self.interval_index = 0
            self.period_index = 0

        main_window.ui.TickerLineEdit.setText(ticker)
        self.set_interval_value()
        self.set_period_value()

        # Start the thread and when finished the work
        self.thread.start()

        # Set up Signals connections
        main_window.ui.IntervalLeft.clicked.connect(self.interval_left_button)
        main_window.ui.IntervalRight.clicked.connect(self.interval_right_button)
        main_window.ui.PeriodLeft.clicked.connect(self.period_left_button)
        main_window.ui.PeriodRight.clicked.connect(self.period_right_button)
        main_window.ui.TickerButton.clicked.connect(self.ticket_button_clicked)
        main_window.ui.TickerLineEdit.textEdited.connect(self.ticker_line_edit)

    # Start the background thread work
    @Slot()
    def start_background_work(self):
        settings = self.main_window.settings
        settings.beginGroup("Ticker")
        ticker = settings.value("ticker", "META", str)
        interval = settings.value("interval", "1m", str)
        period = settings.value("period", "1d", str)
        settings.endGroup()

        self.set_chart_label_text(ticker)
        self.thread.worker.start_fetching_signal.emit(ticker, interval, period)

    @Slot(str)
    def ticker_line_edit(self, text):
        if not text.strip():
            self.main_window.ui.TickerButton.setDisabled(True)
        else:
            self.main_window.ui.TickerButton.setEnabled(True)
            self.main_window.ui.TickerLineEdit.setText(text.upper())

    @Slot()
    def interval_left_button(self):
        self.interval_index = (self.interval_index - 1) % len(self.intervals)
        self.set_interval_value()

    @Slot()
    def interval_right_button(self):
        self.interval_index = (self.interval_index + 1) % len(self.intervals)
        self.set_interval_value()

    @Slot()
    def period_left_button(self):
        self.period_index = (self.period_index - 1) % len(self.periods)
        self.set_period_value()

    @Slot()
    def period_right_button(self):
        self.period_index = (self.period_index + 1) % len(self.periods)
        self.set_period_value()

    def set_interval_value(self):
        text = self.intervals[self.interval_index].removesuffix("m") + " minute"
        if self.interval_index != 0:
            text += "s"
        self.main_window.ui.IntervalValue.setText(text)

    def set_period_value(self):
        text = self.periods[self.period_index].removesuffix("d") + " day"
        if self.period_index != 0:
            text += "s"
        self.main_window.ui.PeriodValue.setText(text)

    @Slot()
    def ticket_button_clicked(self):
        settings = self.main_window.settings

        ticker = self.main_window.ui.TickerLineEdit.text().strip().upper()
        interval = self.intervals[self.interval_index]
        period = self.periods[self.period_index]

        worker = self.thread.worker

        # Only start a new work if any data changes
        if not ticker or (worker.tickers == ticker and worker.interval == interval and worker.period == period):
            return

        # Clear info boxes
        ui = self.main_window.ui
        ui.CloseValue.setText("")
        ui.OpenValue.setText("")
        ui.VolumeValue.setText("")
        ui.RangeValue.setText("")
        ui.HighestCloseValue.setText("")
        ui.LowestCloseValue.setText("")
        ui.AvgVolumeValue.setText("")

        self.set_chart_label_text(ticker)

        # Start the work with the new data and save the settings
        self.ticker_changed.emit()
        self.thread.timer.stop()
        self.thread.worker.start_fetching_signal.emit(ticker, interval, period)
        settings.beginGroup("Ticker")
        settings.setValue("ticker", ticker)
        settings.setValue("interval", interval)
        settings.setValue("period", period)
        settings.endGroup()

    # Set the text in the label in the top menu bar
    def set_chart_label_text(self, ticker):
        interval = self.intervals[self.interval_index].removesuffix("m") + " minute"
        if self.interval_index != 0:
            interval += "s"

        period = self.periods[self.period_index].removesuffix("d") + " day"
        if self.period_index != 0:
            period += "s"

        chart_text = "Ticker: " + ticker + "#" + "Interval: " + interval + "#" + "Period: " + period
        chart_text = chart_text.replace("#", "        ")
        self.main_window.ui.ChartLabel.setText(chart_text)
