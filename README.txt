Stock Price App
Description:
The app display the chart of the stock price of a particular ticket in the selected interval and period.
The chart is updated every minute with the latest information ensuring the latest data to be displayed.

Features:
Interactive Chart: Visualizes stock prices within specified periods and intervals.
Informative Boxes: Presents real-time data corresponding to the displayed chart.
Real Time Updates: Update the data each minutes to display the latest data available.
Theme Customization: Allows to personalize the application's visual style according to predefined styles.

How does it work:
The app showcases selected stock prices through real-time chart updates.
A background thread continuously retrieves data, updating the UI every minute.

Tools used:
PyCharm
Qt Designer
Python 3.12.2

App Architecture:
Stock Price App/
│
├── __main__.py The main file.
│
├── src/
│   ├── Constants.py - Contains all constants used in the application
│   ├── stock_price.py
│   └── ui/ - Directory containing all UI-related files
│       ├── generated/ - Directory containing files generated from *.ui and *.qrc files
│       ├── mainwindow.py
│       └── ... (other UI-related files)
│
└── ui/
    ├── MainWindow.ui - Main User Interface
    ├── InfoWindow.ui - Info Window
    ├── resource.qrc
    ├── qss/ - Directory containing style files used by the app
    └── icons/ - Directory containing all icons used in the app


Requirements:
PySide6~=6.6.2
pandas~=2.2.0
# used by pandas from version 3.0
Pyarrow~=15.0.0
yfinance~=0.2.36

You can install all required dependencies by executing:
pip install -r requirements.txt

Project Setup with PyCharm:
1- Open a PyCharm project within this folder (it will prompt to create a virtual environment, which is suggested).
2- Install all requirements (if not already done by PyCharm).
3- Run the commands in the section below ** (In case you see no icons)
4- Run the __main__.py file.

Normal Setup:
0- Install Python (if not already installed).
1- Install all requirements.
2- Run the commands in the section below ** (In case you see no icons)
3- Run the __main__.py file.

How to do in PyCharm with a virtual environment:
How to open Qt Designer (to see the *.ui files) (PySide needed)
In terminal within this folder
pyside6-designer.exe

** How to convert a *.ui file (PySide needed)
In terminal within this folder
pyside6-uic.exe --from-imports ui\mainwindow.ui -o src\ui\generated\ui_mainwindow.py
pyside6-uic.exe --from-imports ui\infowindow.ui -o src\ui\generated\ui_infowindow.py

** How to convert a *.qrc file (PySide needed)
In terminal within this folder
pyside6-rcc ui\resource.qrc -o src\ui\generated\resource_rc.py