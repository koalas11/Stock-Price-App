import yfinance as yf

from PySide6.QtCore import QThread, QTimer, Slot, QObject, Signal, Qt


# WorkerThread class, handle the background work of the application
# Run the worker every minute ensuring the data is up-to-date
# Use a Slot & Signal architecture to change thread for the background work
class WorkerThread(QThread):
    timer = QTimer()
    start_timer_signal = Signal()

    def __init__(self, finish_signal, update_chart, loading_end):
        super().__init__()
        self.finish_signal = finish_signal
        self.update_chart = update_chart
        self.loading_end = loading_end
        self.worker = None
        self.start_timer_signal.connect(self.start_timer, type=Qt.ConnectionType.QueuedConnection)

    def run(self):
        self.worker = Worker(self.start_timer_signal, self.update_chart, self.loading_end)
        self.worker.start_fetching_signal.connect(self.worker.start_fetch, type=Qt.ConnectionType.QueuedConnection)
        self.timer.timeout.connect(self.worker.fetch, type=Qt.ConnectionType.QueuedConnection)
        self.finish_signal.emit()
        self.exec()

    @Slot()
    def stop(self):
        self.timer.stop()
        self.quit()

    @Slot(int)
    def start_timer(self):
        self.timer.start(60000)


# Worker class, handle the work
# Fetch the latest data by the given arguments and send the data to the UI
class Worker(QObject):
    start_fetching_signal = Signal(str, str, str)

    def __init__(self, start_timer_signal, update_chart, loading_end):
        super().__init__()
        self.start_timer_signal = start_timer_signal
        self.update_chart = update_chart
        self.loading_end = loading_end
        self.tickers = None
        self.interval = None
        self.period = None

    # Start the fetch and the timer
    @Slot(str, str, str)
    def start_fetch(self, tickers, interval, period):
        self.tickers = tickers
        self.interval = interval
        self.period = period
        check = self.fetch()
        if check is None:
            self.loading_end.emit(True)
            self.start_timer_signal.emit()
        else:
            self.loading_end.emit(False)

    # Fetch data
    @Slot()
    def fetch(self):
        result = yf.download(self.tickers, interval=self.interval, period=self.period)
        if len(result) > 1:
            self.update_chart.emit(result)
        else:
            return False
