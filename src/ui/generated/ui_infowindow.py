# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infowindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_InfoForm(object):
    def setupUi(self, InfoForm):
        if not InfoForm.objectName():
            InfoForm.setObjectName(u"InfoForm")
        InfoForm.resize(251, 185)
        self.verticalLayout = QVBoxLayout(InfoForm)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.MainWidget = QWidget(InfoForm)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainLayout = QVBoxLayout(self.MainWidget)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.MainLayout.setContentsMargins(9, 0, 9, 0)
        self.InfoLabel = QLabel(self.MainWidget)
        self.InfoLabel.setObjectName(u"InfoLabel")
        font = QFont()
        font.setPointSize(16)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setAlignment(Qt.AlignCenter)

        self.MainLayout.addWidget(self.InfoLabel)

        self.ConfigLayout = QHBoxLayout()
        self.ConfigLayout.setObjectName(u"ConfigLayout")
        self.ConfigLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.ConfigLabel = QLabel(self.MainWidget)
        self.ConfigLabel.setObjectName(u"ConfigLabel")

        self.ConfigLayout.addWidget(self.ConfigLabel)

        self.ConfigValue = QLabel(self.MainWidget)
        self.ConfigValue.setObjectName(u"ConfigValue")

        self.ConfigLayout.addWidget(self.ConfigValue)


        self.MainLayout.addLayout(self.ConfigLayout)

        self.VersionLabel = QLabel(self.MainWidget)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setAlignment(Qt.AlignCenter)

        self.MainLayout.addWidget(self.VersionLabel)


        self.verticalLayout.addWidget(self.MainWidget)


        self.retranslateUi(InfoForm)

        QMetaObject.connectSlotsByName(InfoForm)
    # setupUi

    def retranslateUi(self, InfoForm):
        InfoForm.setWindowTitle(QCoreApplication.translate("InfoForm", u"Info Stock Price App", None))
        self.InfoLabel.setText(QCoreApplication.translate("InfoForm", u"Info", None))
        self.ConfigLabel.setText(QCoreApplication.translate("InfoForm", u"Config Path:", None))
        self.ConfigValue.setText("")
        self.VersionLabel.setText(QCoreApplication.translate("InfoForm", u"Stock Price App\n"
"Version 1.0", None))
    # retranslateUi

