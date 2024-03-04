from PySide6 import QtCharts
from PySide6.QtCharts import QChartView
from PySide6.QtCore import Slot, QDateTime, Qt, QPoint
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import QLabel, QGraphicsEllipseItem
from pandas import DataFrame


def convert_date(date):
    date = QDateTime.fromString(str(date.isoformat()), Qt.ISODate)
    return date.toLocalTime()


# StockChart class, handle the Chart setup
class StockChart(QChartView):
    def __init__(self, update_info_signal):
        super().__init__()
        self.data_frame = None
        self.series = None
        self.update_info_signal = update_info_signal
        self.setContentsMargins(0, 0, 0, 0)

        # Add Tooltip Label and Point to the Chart
        self.label = QLabel(self)
        self.label.setObjectName("ChartLabel")
        self.label.hide()

        self.point = QGraphicsEllipseItem(-5, -5, 10, 10)
        self.point.setBrush(QBrush(QColor(Qt.red)))
        self.point.hide()
        self.scene().addItem(self.point)
        self.point.setZValue(1)

        # Dummy series to show the dates in the x-axis
        dummy_series = QtCharts.QLineSeries()
        self.line_chart = QtCharts.QChart()
        self.line_chart.setContentsMargins(0, 0, 0, 0)
        self.line_chart.legend().hide()
        self.line_chart.addSeries(dummy_series)

        # Set up the axes
        self.date_axis = QtCharts.QDateTimeAxis()
        self.date_axis.setFormat("dd-MM-yyyy h:mm")
        self.date_axis.setTitleText("Timeline")
        self.date_axis.setTickCount(2)

        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.hide()
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTitleText("Stock Price")

        self.line_chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.line_chart.addAxis(self.date_axis, Qt.AlignBottom)
        self.line_chart.addAxis(self.axis_y, Qt.AlignLeft)

        dummy_series.attachAxis(self.date_axis)

        self.setChart(self.line_chart)
        self.setRenderHint(QPainter.Antialiasing)

    @Slot(str)
    def theme_changed(self, style):
        self.label.setStyleSheet(style)

    # Updates the chart with the data given
    @Slot(DataFrame)
    def update_chart(self, data_frame):
        assert isinstance(data_frame, DataFrame)
        self.data_frame = data_frame
        new_series = QtCharts.QLineSeries()
        max_val = float('-inf')
        min_val = float('inf')
        sum_volume = 0

        # Add element to the Series
        for index, x in enumerate(data_frame.index):
            value = data_frame["Adj Close"][x]
            sum_volume += data_frame["Volume"][x].astype(int)
            new_series.append(index, value)
            if value > max_val:
                max_val = value
            elif value < min_val:
                min_val = value

        index_last = len(data_frame) - 1

        # Update the Axes
        first_date = convert_date(data_frame.index[0])
        last_date = convert_date(data_frame.index[index_last])
        self.date_axis.setRange(first_date, last_date)

        self.axis_x.setRange(0, index_last)
        self.axis_y.setRange(min_val - 2, max_val + 2)

        # Update the Series
        if self.series is not None:
            self.line_chart.removeSeries(self.series)
        self.series = new_series
        self.line_chart.addSeries(self.series)

        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        # Show new info
        close_val = str(round(data_frame["Adj Close"].iloc[index_last], 2))
        open_val = str(round(data_frame["Open"].iloc[index_last], 2))
        volume_val = str(round(data_frame["Volume"].iloc[index_last]))
        range_val = (str(round(data_frame["Adj Close"].iloc[0], 2)) + " - " +
                     str(round(data_frame["Adj Close"].iloc[index_last], 2)))
        min_val = str(round(min_val, 2))
        max_val = str(round(max_val, 2))
        avg_val = str(round(sum_volume / len(data_frame), 2))

        self.update_info_signal.emit(close_val, open_val, volume_val, range_val, min_val, max_val, avg_val)

    # Show a tooltip showing the info of that point when hovering on the chart
    def mouseMoveEvent(self, event):
        # Get position of the value in the chart
        mouse_pos = self.mapFromGlobal(event.globalPos())
        x_value = self.chart().mapToValue(mouse_pos, self.series).x()

        index = round(x_value)

        if index < 0 or index > (len(self.data_frame) - 1):
            self.label.hide()
            self.point.hide()
            super().mouseMoveEvent(event)
            return

        pos = self.chart().mapToPosition(self.series.at(index), self.series)

        # Prepare Label text
        date = convert_date(self.data_frame.index[index]).toString("dd-MM-yyyy h:mm")
        row = self.data_frame.iloc[index]
        open_val = str(round(row["Open"], 2))
        high_val = str(round(row["High"], 2))
        low_val = str(round(row["Low"], 2))
        close_val = str(round(row["Adj Close"], 2))
        volume_val = str(row["Volume"].astype(int))

        text = "Date: " + date + "\nOpen: " + open_val + "\nHigh: " + high_val + "\nLow: " + low_val
        text += "\nClose: " + close_val + "\nVolume: " + volume_val
        self.label.setText(text)

        # Set Label and Point position and show them
        height = 5

        if self.series.at(index).y() > ((self.axis_y.max() + self.axis_y.min()) / 2):
            height = (self.label.height() + 10) * -1

        self.label.move(pos.toPoint() - QPoint(self.label.width() // 2, self.label.height() + height))
        self.point.setPos(pos)
        self.label.show()
        self.point.show()
        super().mouseMoveEvent(event)

    def leaveEvent(self, event):
        self.label.hide()
        self.point.hide()
        super().leaveEvent(event)
