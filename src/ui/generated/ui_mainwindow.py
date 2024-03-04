# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icons/icons/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.MenuLayout = QHBoxLayout()
        self.MenuLayout.setObjectName(u"MenuLayout")
        self.MenuLayout.setContentsMargins(-1, 0, -1, -1)
        self.MenuButton = QPushButton(self.centralwidget)
        self.MenuButton.setObjectName(u"MenuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuButton.sizePolicy().hasHeightForWidth())
        self.MenuButton.setSizePolicy(sizePolicy)
        self.MenuButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuButton.setIcon(icon1)

        self.MenuLayout.addWidget(self.MenuButton)

        self.MenuLabel = QLabel(self.centralwidget)
        self.MenuLabel.setObjectName(u"MenuLabel")

        self.MenuLayout.addWidget(self.MenuLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MenuLayout.addItem(self.horizontalSpacer_3)

        self.ChartLabel = QLabel(self.centralwidget)
        self.ChartLabel.setObjectName(u"ChartLabel")

        self.MenuLayout.addWidget(self.ChartLabel)

        self.MenuSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MenuLayout.addItem(self.MenuSpacer_2)

        self.AutoUpdateLabel = QLabel(self.centralwidget)
        self.AutoUpdateLabel.setObjectName(u"AutoUpdateLabel")

        self.MenuLayout.addWidget(self.AutoUpdateLabel)


        self.verticalLayout_4.addLayout(self.MenuLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.MainLayout = QHBoxLayout()
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftBarWidget = QWidget(self.centralwidget)
        self.LeftBarWidget.setObjectName(u"LeftBarWidget")
        self.LeftBarLayout_2 = QHBoxLayout(self.LeftBarWidget)
        self.LeftBarLayout_2.setObjectName(u"LeftBarLayout_2")
        self.LeftBarLayout_2.setContentsMargins(1, -1, 1, -1)
        self.LeftBarMainLayout = QHBoxLayout()
        self.LeftBarMainLayout.setObjectName(u"LeftBarMainLayout")
        self.LeftBarMainLayout.setContentsMargins(-1, -1, 0, -1)
        self.LeftBarLayout = QVBoxLayout()
        self.LeftBarLayout.setObjectName(u"LeftBarLayout")
        self.LeftBarLayout.setContentsMargins(-1, -1, 0, -1)
        self.GoBackButton = QCommandLinkButton(self.LeftBarWidget)
        self.GoBackButton.setObjectName(u"GoBackButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/go_back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.GoBackButton.setIcon(icon2)

        self.LeftBarLayout.addWidget(self.GoBackButton)

        self.LeftBarStackedWidget = QStackedWidget(self.LeftBarWidget)
        self.LeftBarStackedWidget.setObjectName(u"LeftBarStackedWidget")
        self.MenuBarPage = QWidget()
        self.MenuBarPage.setObjectName(u"MenuBarPage")
        self.verticalLayout_5 = QVBoxLayout(self.MenuBarPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MenuLabel_2 = QLabel(self.MenuBarPage)
        self.MenuLabel_2.setObjectName(u"MenuLabel_2")
        font = QFont()
        font.setPointSize(14)
        self.MenuLabel_2.setFont(font)
        self.MenuLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.MenuLabel_2)

        self.SettingsButton = QCommandLinkButton(self.MenuBarPage)
        self.SettingsButton.setObjectName(u"SettingsButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsButton.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.SettingsButton)

        self.InfoButton = QCommandLinkButton(self.MenuBarPage)
        self.InfoButton.setObjectName(u"InfoButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.InfoButton.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.InfoButton)

        self.MenuSpacer = QSpacerItem(20, 399, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.MenuSpacer)

        self.VersionLabel = QLabel(self.MenuBarPage)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.VersionLabel)

        self.LeftBarStackedWidget.addWidget(self.MenuBarPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.verticalLayout_6 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SettingsLabel = QLabel(self.SettingsPage)
        self.SettingsLabel.setObjectName(u"SettingsLabel")
        self.SettingsLabel.setFont(font)
        self.SettingsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.SettingsLabel)

        self.ThemeLayout = QHBoxLayout()
        self.ThemeLayout.setObjectName(u"ThemeLayout")
        self.ThemeLayout.setContentsMargins(-1, 0, -1, -1)
        self.SunIcon = QLabel(self.SettingsPage)
        self.SunIcon.setObjectName(u"SunIcon")
        self.SunIcon.setPixmap(QPixmap(u":/icons/icons/sun.svg"))

        self.ThemeLayout.addWidget(self.SunIcon)

        self.ThemeLabel = QLabel(self.SettingsPage)
        self.ThemeLabel.setObjectName(u"ThemeLabel")
        self.ThemeLabel.setAlignment(Qt.AlignCenter)

        self.ThemeLayout.addWidget(self.ThemeLabel)

        self.MoonIcon = QLabel(self.SettingsPage)
        self.MoonIcon.setObjectName(u"MoonIcon")
        self.MoonIcon.setPixmap(QPixmap(u":/icons/icons/moon.svg"))
        self.MoonIcon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.ThemeLayout.addWidget(self.MoonIcon)


        self.verticalLayout_6.addLayout(self.ThemeLayout)

        self.ThemeComboBox = QComboBox(self.SettingsPage)
        self.ThemeComboBox.setObjectName(u"ThemeComboBox")

        self.verticalLayout_6.addWidget(self.ThemeComboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.LeftBarStackedWidget.addWidget(self.SettingsPage)

        self.LeftBarLayout.addWidget(self.LeftBarStackedWidget)


        self.LeftBarMainLayout.addLayout(self.LeftBarLayout)

        self.MenuBarLine = QFrame(self.LeftBarWidget)
        self.MenuBarLine.setObjectName(u"MenuBarLine")
        self.MenuBarLine.setMinimumSize(QSize(0, 0))
        self.MenuBarLine.setFrameShape(QFrame.VLine)
        self.MenuBarLine.setFrameShadow(QFrame.Sunken)

        self.LeftBarMainLayout.addWidget(self.MenuBarLine)


        self.LeftBarLayout_2.addLayout(self.LeftBarMainLayout)


        self.MainLayout.addWidget(self.LeftBarWidget)

        self.ContentMainLayout = QVBoxLayout()
        self.ContentMainLayout.setObjectName(u"ContentMainLayout")
        self.MainContainer = QWidget(self.centralwidget)
        self.MainContainer.setObjectName(u"MainContainer")
        self.MainContainer.setEnabled(True)

        self.ContentMainLayout.addWidget(self.MainContainer)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.ContentMainLayout.addItem(self.verticalSpacer)

        self.InfoLayout = QHBoxLayout()
        self.InfoLayout.setObjectName(u"InfoLayout")
        self.InfoLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.InfoLayout.setContentsMargins(-1, -1, 0, -1)
        self.LatestInfoGroupBox = QGroupBox(self.centralwidget)
        self.LatestInfoGroupBox.setObjectName(u"LatestInfoGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LatestInfoGroupBox.sizePolicy().hasHeightForWidth())
        self.LatestInfoGroupBox.setSizePolicy(sizePolicy1)
        self.LatestInfoGroupBox.setAlignment(Qt.AlignCenter)
        self.LatestInfoGroupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.LatestInfoGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LatestInfoLayout = QVBoxLayout()
        self.LatestInfoLayout.setObjectName(u"LatestInfoLayout")
        self.LatestInfoLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.LatestInfoLayout.setContentsMargins(0, -1, -1, -1)
        self.CloseLayout = QHBoxLayout()
        self.CloseLayout.setObjectName(u"CloseLayout")
        self.CloseLayout.setContentsMargins(9, -1, 9, -1)
        self.CloseLabel = QLabel(self.LatestInfoGroupBox)
        self.CloseLabel.setObjectName(u"CloseLabel")

        self.CloseLayout.addWidget(self.CloseLabel)

        self.CloseValue = QLabel(self.LatestInfoGroupBox)
        self.CloseValue.setObjectName(u"CloseValue")

        self.CloseLayout.addWidget(self.CloseValue)


        self.LatestInfoLayout.addLayout(self.CloseLayout)

        self.OpenLayout = QHBoxLayout()
        self.OpenLayout.setObjectName(u"OpenLayout")
        self.OpenLayout.setContentsMargins(9, -1, 9, -1)
        self.OpenLabel = QLabel(self.LatestInfoGroupBox)
        self.OpenLabel.setObjectName(u"OpenLabel")

        self.OpenLayout.addWidget(self.OpenLabel)

        self.OpenValue = QLabel(self.LatestInfoGroupBox)
        self.OpenValue.setObjectName(u"OpenValue")

        self.OpenLayout.addWidget(self.OpenValue)


        self.LatestInfoLayout.addLayout(self.OpenLayout)

        self.VolumeLayout = QHBoxLayout()
        self.VolumeLayout.setObjectName(u"VolumeLayout")
        self.VolumeLayout.setContentsMargins(9, -1, 9, -1)
        self.VolumeLabel = QLabel(self.LatestInfoGroupBox)
        self.VolumeLabel.setObjectName(u"VolumeLabel")

        self.VolumeLayout.addWidget(self.VolumeLabel)

        self.VolumeValue = QLabel(self.LatestInfoGroupBox)
        self.VolumeValue.setObjectName(u"VolumeValue")

        self.VolumeLayout.addWidget(self.VolumeValue)


        self.LatestInfoLayout.addLayout(self.VolumeLayout)

        self.RangeLayout = QHBoxLayout()
        self.RangeLayout.setObjectName(u"RangeLayout")
        self.RangeLayout.setContentsMargins(9, -1, 9, -1)
        self.RangeLabel = QLabel(self.LatestInfoGroupBox)
        self.RangeLabel.setObjectName(u"RangeLabel")
        sizePolicy1.setHeightForWidth(self.RangeLabel.sizePolicy().hasHeightForWidth())
        self.RangeLabel.setSizePolicy(sizePolicy1)

        self.RangeLayout.addWidget(self.RangeLabel)

        self.RangeValue = QLabel(self.LatestInfoGroupBox)
        self.RangeValue.setObjectName(u"RangeValue")

        self.RangeLayout.addWidget(self.RangeValue)


        self.LatestInfoLayout.addLayout(self.RangeLayout)


        self.verticalLayout.addLayout(self.LatestInfoLayout)


        self.InfoLayout.addWidget(self.LatestInfoGroupBox)

        self.horizontalSpacer = QSpacerItem(6, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InfoLayout.addItem(self.horizontalSpacer)

        self.ExtraInfoGroupBox = QGroupBox(self.centralwidget)
        self.ExtraInfoGroupBox.setObjectName(u"ExtraInfoGroupBox")
        sizePolicy1.setHeightForWidth(self.ExtraInfoGroupBox.sizePolicy().hasHeightForWidth())
        self.ExtraInfoGroupBox.setSizePolicy(sizePolicy1)
        self.ExtraInfoGroupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.ExtraInfoGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.HighestCloseLayout = QHBoxLayout()
        self.HighestCloseLayout.setObjectName(u"HighestCloseLayout")
        self.HighestCloseLayout.setContentsMargins(9, -1, 9, -1)
        self.HighestCloseLabel = QLabel(self.ExtraInfoGroupBox)
        self.HighestCloseLabel.setObjectName(u"HighestCloseLabel")
        sizePolicy1.setHeightForWidth(self.HighestCloseLabel.sizePolicy().hasHeightForWidth())
        self.HighestCloseLabel.setSizePolicy(sizePolicy1)
        self.HighestCloseLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HighestCloseLayout.addWidget(self.HighestCloseLabel)

        self.HighestCloseValue = QLabel(self.ExtraInfoGroupBox)
        self.HighestCloseValue.setObjectName(u"HighestCloseValue")
        sizePolicy1.setHeightForWidth(self.HighestCloseValue.sizePolicy().hasHeightForWidth())
        self.HighestCloseValue.setSizePolicy(sizePolicy1)

        self.HighestCloseLayout.addWidget(self.HighestCloseValue)


        self.verticalLayout_7.addLayout(self.HighestCloseLayout)

        self.LowestCloseLayout = QHBoxLayout()
        self.LowestCloseLayout.setObjectName(u"LowestCloseLayout")
        self.LowestCloseLayout.setContentsMargins(9, -1, 9, -1)
        self.LowestCloseLabel = QLabel(self.ExtraInfoGroupBox)
        self.LowestCloseLabel.setObjectName(u"LowestCloseLabel")
        sizePolicy1.setHeightForWidth(self.LowestCloseLabel.sizePolicy().hasHeightForWidth())
        self.LowestCloseLabel.setSizePolicy(sizePolicy1)
        self.LowestCloseLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LowestCloseLayout.addWidget(self.LowestCloseLabel)

        self.LowestCloseValue = QLabel(self.ExtraInfoGroupBox)
        self.LowestCloseValue.setObjectName(u"LowestCloseValue")
        sizePolicy1.setHeightForWidth(self.LowestCloseValue.sizePolicy().hasHeightForWidth())
        self.LowestCloseValue.setSizePolicy(sizePolicy1)

        self.LowestCloseLayout.addWidget(self.LowestCloseValue)


        self.verticalLayout_7.addLayout(self.LowestCloseLayout)

        self.AvgVolumeLayout = QHBoxLayout()
        self.AvgVolumeLayout.setObjectName(u"AvgVolumeLayout")
        self.AvgVolumeLabel = QLabel(self.ExtraInfoGroupBox)
        self.AvgVolumeLabel.setObjectName(u"AvgVolumeLabel")

        self.AvgVolumeLayout.addWidget(self.AvgVolumeLabel)

        self.AvgVolumeValue = QLabel(self.ExtraInfoGroupBox)
        self.AvgVolumeValue.setObjectName(u"AvgVolumeValue")

        self.AvgVolumeLayout.addWidget(self.AvgVolumeValue)


        self.verticalLayout_7.addLayout(self.AvgVolumeLayout)


        self.InfoLayout.addWidget(self.ExtraInfoGroupBox)

        self.horizontalSpacer_2 = QSpacerItem(6, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.InfoLayout.addItem(self.horizontalSpacer_2)

        self.TickerGroupBox = QGroupBox(self.centralwidget)
        self.TickerGroupBox.setObjectName(u"TickerGroupBox")
        self.TickerGroupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.TickerGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TickerMainLayout = QVBoxLayout()
        self.TickerMainLayout.setObjectName(u"TickerMainLayout")
        self.TickerMainLayout.setContentsMargins(9, -1, 9, -1)
        self.TickerLayout = QVBoxLayout()
        self.TickerLayout.setObjectName(u"TickerLayout")
        self.TickerLineEdit = QLineEdit(self.TickerGroupBox)
        self.TickerLineEdit.setObjectName(u"TickerLineEdit")

        self.TickerLayout.addWidget(self.TickerLineEdit)


        self.TickerMainLayout.addLayout(self.TickerLayout)

        self.IntervalMainLayout = QVBoxLayout()
        self.IntervalMainLayout.setObjectName(u"IntervalMainLayout")
        self.IntervalLabel = QLabel(self.TickerGroupBox)
        self.IntervalLabel.setObjectName(u"IntervalLabel")
        self.IntervalLabel.setAlignment(Qt.AlignCenter)

        self.IntervalMainLayout.addWidget(self.IntervalLabel)

        self.IntervalLayout = QHBoxLayout()
        self.IntervalLayout.setObjectName(u"IntervalLayout")
        self.IntervalLeft = QPushButton(self.TickerGroupBox)
        self.IntervalLeft.setObjectName(u"IntervalLeft")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IntervalLeft.setIcon(icon5)

        self.IntervalLayout.addWidget(self.IntervalLeft)

        self.IntervalValue = QLabel(self.TickerGroupBox)
        self.IntervalValue.setObjectName(u"IntervalValue")
        self.IntervalValue.setAlignment(Qt.AlignCenter)

        self.IntervalLayout.addWidget(self.IntervalValue)

        self.IntervalRight = QPushButton(self.TickerGroupBox)
        self.IntervalRight.setObjectName(u"IntervalRight")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IntervalRight.setIcon(icon6)

        self.IntervalLayout.addWidget(self.IntervalRight)


        self.IntervalMainLayout.addLayout(self.IntervalLayout)


        self.TickerMainLayout.addLayout(self.IntervalMainLayout)

        self.PeriodMainLayout = QVBoxLayout()
        self.PeriodMainLayout.setObjectName(u"PeriodMainLayout")
        self.PeriodMainLayout.setContentsMargins(-1, 0, -1, -1)
        self.PeriodLabel = QLabel(self.TickerGroupBox)
        self.PeriodLabel.setObjectName(u"PeriodLabel")
        self.PeriodLabel.setAlignment(Qt.AlignCenter)

        self.PeriodMainLayout.addWidget(self.PeriodLabel)

        self.PeriodLayout = QHBoxLayout()
        self.PeriodLayout.setObjectName(u"PeriodLayout")
        self.PeriodLayout.setContentsMargins(-1, 0, -1, -1)
        self.PeriodLeft = QPushButton(self.TickerGroupBox)
        self.PeriodLeft.setObjectName(u"PeriodLeft")
        self.PeriodLeft.setIcon(icon5)

        self.PeriodLayout.addWidget(self.PeriodLeft)

        self.PeriodValue = QLabel(self.TickerGroupBox)
        self.PeriodValue.setObjectName(u"PeriodValue")
        self.PeriodValue.setAlignment(Qt.AlignCenter)

        self.PeriodLayout.addWidget(self.PeriodValue)

        self.PeriodRight = QPushButton(self.TickerGroupBox)
        self.PeriodRight.setObjectName(u"PeriodRight")
        self.PeriodRight.setIcon(icon6)

        self.PeriodLayout.addWidget(self.PeriodRight)


        self.PeriodMainLayout.addLayout(self.PeriodLayout)


        self.TickerMainLayout.addLayout(self.PeriodMainLayout)

        self.TickerButton = QPushButton(self.TickerGroupBox)
        self.TickerButton.setObjectName(u"TickerButton")

        self.TickerMainLayout.addWidget(self.TickerButton)


        self.verticalLayout_3.addLayout(self.TickerMainLayout)


        self.InfoLayout.addWidget(self.TickerGroupBox)

        self.InfoLayout.setStretch(0, 1)
        self.InfoLayout.setStretch(2, 1)
        self.InfoLayout.setStretch(4, 1)

        self.ContentMainLayout.addLayout(self.InfoLayout)

        self.ContentMainLayout.setStretch(0, 5)
        self.ContentMainLayout.setStretch(2, 2)

        self.MainLayout.addLayout(self.ContentMainLayout)

        self.MainLayout.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.MainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.GoBackButton.clicked.connect(self.GoBackButton.hide)
        self.GoBackButton.clicked["bool"].connect(self.GoBackButton.setEnabled)

        self.LeftBarStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stock Price App", None))
        self.MenuButton.setText("")
#if QT_CONFIG(shortcut)
        self.MenuButton.setShortcut(QCoreApplication.translate("MainWindow", u"M", None))
#endif // QT_CONFIG(shortcut)
        self.MenuLabel.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.ChartLabel.setText("")
        self.AutoUpdateLabel.setText(QCoreApplication.translate("MainWindow", u"The chart is always up-to-date", None))
        self.GoBackButton.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.MenuLabel_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.InfoButton.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.VersionLabel.setText(QCoreApplication.translate("MainWindow", u"Stock Price App\n"
"Version 1.0", None))
        self.SettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.SunIcon.setText("")
        self.ThemeLabel.setText(QCoreApplication.translate("MainWindow", u"Themes", None))
        self.MoonIcon.setText("")
        self.LatestInfoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Latest Info", None))
        self.CloseLabel.setText(QCoreApplication.translate("MainWindow", u"Close:", None))
        self.CloseValue.setText("")
        self.OpenLabel.setText(QCoreApplication.translate("MainWindow", u"Open:", None))
        self.OpenValue.setText("")
        self.VolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
        self.VolumeValue.setText("")
        self.RangeLabel.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.RangeValue.setText("")
        self.ExtraInfoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Extra Info", None))
        self.HighestCloseLabel.setText(QCoreApplication.translate("MainWindow", u"Highest Close:", None))
        self.HighestCloseValue.setText("")
        self.LowestCloseLabel.setText(QCoreApplication.translate("MainWindow", u"Lowest Close:", None))
        self.LowestCloseValue.setText("")
        self.AvgVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Average Volume:", None))
        self.AvgVolumeValue.setText("")
        self.TickerGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ticker", None))
        self.TickerLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ticker", None))
        self.IntervalLabel.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.IntervalLeft.setText("")
        self.IntervalValue.setText("")
        self.IntervalRight.setText("")
        self.PeriodLabel.setText(QCoreApplication.translate("MainWindow", u"Period", None))
        self.PeriodLeft.setText("")
        self.PeriodValue.setText("")
        self.PeriodRight.setText("")
        self.TickerButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

