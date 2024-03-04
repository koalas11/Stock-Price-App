from typing import TYPE_CHECKING

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import QWidget, QLabel

from .stockchart import StockChart

if TYPE_CHECKING:
    from .mainwindow import MainWindow


# MainContainer class, handle the setup of the Main Container (where the chart is displayed)
class MainContainer(QWidget):
    update_info_signal = Signal(str, str, str, str, str, str, str)

    def __init__(self, parent: 'MainWindow'):
        super().__init__(parent.ui.MainContainer)
        self.ui = parent.ui
        self.setContentsMargins(0, 0, 0, 0)
        main_layout = QtWidgets.QVBoxLayout()
        parent.ui.MainContainer.setLayout(main_layout)

        # Set up the Chart and the container
        self.chart = StockChart(self.update_info_signal)

        self.loading = QLabel()
        self.loading.setText("Loading...")
        self.loading.setAlignment(Qt.AlignCenter)
        font = self.loading.font()
        font.setPointSize(42)
        self.loading.setFont(font)

        self.error = QLabel()
        self.error.setAlignment(Qt.AlignCenter)
        font = self.error.font()
        font.setPointSize(18)
        self.error.setFont(font)

        main_layout.addWidget(self.chart)
        main_layout.addWidget(self.loading)
        main_layout.addWidget(self.error)

        self.error.hide()
        self.chart.hide()
        self.loading.show()

        self.update_info_signal.connect(self.update_info)

    @Slot(str)
    def theme_changed(self, style):
        self.chart.setStyleSheet(style)
        self.loading.setStyleSheet(style)
        self.error.setStyleSheet(style)

    # Updates the Latest info box and the Extra info box
    @Slot(str, str, str, str, str, str, str)
    def update_info(self, close_val, open_val, volume_val, range_val, lowest_val, highest_val, avg_val):
        self.ui.CloseValue.setText(close_val)
        self.ui.OpenValue.setText(open_val)
        self.ui.VolumeValue.setText(volume_val)
        self.ui.RangeValue.setText(range_val)
        self.ui.LowestCloseValue.setText(lowest_val)
        self.ui.HighestCloseValue.setText(highest_val)
        self.ui.AvgVolumeValue.setText(avg_val)

    @Slot()
    def hide_chart(self):
        self.chart.hide()
        self.error.hide()
        self.loading.show()

    @Slot(bool)
    def show_chart(self, state):
        self.loading.hide()
        if state:
            self.error.hide()
            self.chart.show()
        else:
            self.error.setText("Not enough data with the provided arguments could be found.\n"
                               "Or the provided ticker is wrong.\n"
                               "Try again with new arguments.")
            self.error.show()
