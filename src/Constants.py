import os

from PySide6.QtCore import QStandardPaths
from PySide6.QtGui import QIcon

# Constant used by the application
APP_NAME = "Stock Price App"
APP_VERSION = "1.0"
CONFIG_START_PATH = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
CONFIG_PATH = os.path.join(CONFIG_START_PATH, "Koalas", "Stock Price App")
CONFIG_FILE = os.path.join(CONFIG_PATH, "config.ini")
APP_ICON = QIcon()
