# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_Raspi.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowTarget(object):
    def setupUi(self, MainWindowTarget):
        MainWindowTarget.setObjectName("MainWindowTarget")
        MainWindowTarget.resize(480, 320)
        MainWindowTarget.setMinimumSize(QtCore.QSize(480, 320))
        MainWindowTarget.setMaximumSize(QtCore.QSize(480, 320))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindowTarget.setPalette(palette)
        MainWindowTarget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindowTarget.setWindowOpacity(1.0)
        MainWindowTarget.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindowTarget)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopSelectionBar = QtWidgets.QHBoxLayout()
        self.TopSelectionBar.setObjectName("TopSelectionBar")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.TopSelectionBar.addItem(spacerItem)
        self.BT_openHomeScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openHomeScreen.setFlat(True)
        self.BT_openHomeScreen.setObjectName("BT_openHomeScreen")
        self.TopSelectionBar.addWidget(self.BT_openHomeScreen)
        self.BT_openSonosScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openSonosScreen.setFlat(True)
        self.BT_openSonosScreen.setObjectName("BT_openSonosScreen")
        self.TopSelectionBar.addWidget(self.BT_openSonosScreen)
        self.BT_openWeatherScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openWeatherScreen.setFlat(True)
        self.BT_openWeatherScreen.setObjectName("BT_openWeatherScreen")
        self.TopSelectionBar.addWidget(self.BT_openWeatherScreen)
        self.BT_openMeteoScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openMeteoScreen.setFlat(True)
        self.BT_openMeteoScreen.setObjectName("BT_openMeteoScreen")
        self.TopSelectionBar.addWidget(self.BT_openMeteoScreen)
        self.BT_openSbbScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openSbbScreen.setFlat(True)
        self.BT_openSbbScreen.setObjectName("BT_openSbbScreen")
        self.TopSelectionBar.addWidget(self.BT_openSbbScreen)
        self.BT_openLogScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_openLogScreen.sizePolicy().hasHeightForWidth())
        self.BT_openLogScreen.setSizePolicy(sizePolicy)
        self.BT_openLogScreen.setMaximumSize(QtCore.QSize(40, 16777215))
        self.BT_openLogScreen.setFlat(True)
        self.BT_openLogScreen.setObjectName("BT_openLogScreen")
        self.TopSelectionBar.addWidget(self.BT_openLogScreen)
        spacerItem1 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.TopSelectionBar.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.TopSelectionBar)
        self.LN_boarderLine = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.LN_boarderLine.setEnabled(False)
        self.LN_boarderLine.setMinimumSize(QtCore.QSize(480, 3))
        self.LN_boarderLine.setAutoFillBackground(False)
        self.LN_boarderLine.setStyleSheet("color: rgb(0, 85, 255)")
        self.LN_boarderLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LN_boarderLine.setLineWidth(3)
        self.LN_boarderLine.setMidLineWidth(3)
        self.LN_boarderLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.LN_boarderLine.setObjectName("LN_boarderLine")
        self.verticalLayout.addWidget(self.LN_boarderLine)
        self.ST_workerStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.ST_workerStack.setGeometry(QtCore.QRect(0, 50, 481, 271))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.ST_workerStack.setPalette(palette)
        self.ST_workerStack.setObjectName("ST_workerStack")
        self.SC_welcomeScreen = QtWidgets.QWidget()
        self.SC_welcomeScreen.setObjectName("SC_welcomeScreen")
        self.WD_clock = QtWidgets.QWidget(self.SC_welcomeScreen)
        self.WD_clock.setGeometry(QtCore.QRect(9, 9, 471, 251))
        self.WD_clock.setObjectName("WD_clock")
        self.WV_clock = QtWebKitWidgets.QWebView(self.WD_clock)
        self.WV_clock.setGeometry(QtCore.QRect(0, 0, 461, 251))
        self.WV_clock.setObjectName("WV_clock")
        self.ST_workerStack.addWidget(self.SC_welcomeScreen)
        self.SC_sonosScreen = QtWidgets.QWidget()
        self.SC_sonosScreen.setObjectName("SC_sonosScreen")
        self.BT_sonosPlay = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_sonosPlay.setGeometry(QtCore.QRect(70, 10, 75, 23))
        self.BT_sonosPlay.setFlat(True)
        self.BT_sonosPlay.setObjectName("BT_sonosPlay")
        self.BT_pause = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_pause.setGeometry(QtCore.QRect(70, 40, 75, 23))
        self.BT_pause.setFlat(True)
        self.BT_pause.setObjectName("BT_pause")
        self.BT_stop = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_stop.setGeometry(QtCore.QRect(70, 70, 75, 23))
        self.BT_stop.setFlat(True)
        self.BT_stop.setObjectName("BT_stop")
        self.BT_skip = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_skip.setGeometry(QtCore.QRect(120, 40, 75, 23))
        self.BT_skip.setFlat(True)
        self.BT_skip.setObjectName("BT_skip")
        self.LB_currentlyPlayingTitle = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingTitle.setGeometry(QtCore.QRect(10, 120, 181, 16))
        self.LB_currentlyPlayingTitle.setObjectName("LB_currentlyPlayingTitle")
        self.BT_previous = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_previous.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.BT_previous.setFlat(True)
        self.BT_previous.setObjectName("BT_previous")
        self.LW_artists = QtWidgets.QListWidget(self.SC_sonosScreen)
        self.LW_artists.setGeometry(QtCore.QRect(210, 10, 261, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 218, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.LW_artists.setPalette(palette)
        self.LW_artists.setObjectName("LW_artists")
        self.SL_volume = QtWidgets.QSlider(self.SC_sonosScreen)
        self.SL_volume.setGeometry(QtCore.QRect(40, 90, 131, 20))
        self.SL_volume.setOrientation(QtCore.Qt.Horizontal)
        self.SL_volume.setObjectName("SL_volume")
        self.LB_currentlyPlayingArtist = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingArtist.setGeometry(QtCore.QRect(10, 140, 191, 16))
        self.LB_currentlyPlayingArtist.setObjectName("LB_currentlyPlayingArtist")
        self.BT_volumeUp = QtWidgets.QToolButton(self.SC_sonosScreen)
        self.BT_volumeUp.setGeometry(QtCore.QRect(180, 90, 21, 21))
        self.BT_volumeUp.setObjectName("BT_volumeUp")
        self.BT_volumeDown = QtWidgets.QToolButton(self.SC_sonosScreen)
        self.BT_volumeDown.setGeometry(QtCore.QRect(10, 90, 21, 21))
        self.BT_volumeDown.setObjectName("BT_volumeDown")
        self.LB_currentlyPlayingPosition = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingPosition.setGeometry(QtCore.QRect(10, 160, 181, 16))
        self.LB_currentlyPlayingPosition.setObjectName("LB_currentlyPlayingPosition")
        self.LB_currentlyPlayingTotal = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingTotal.setGeometry(QtCore.QRect(10, 180, 181, 16))
        self.LB_currentlyPlayingTotal.setObjectName("LB_currentlyPlayingTotal")
        self.LB_currentlyPlayingCurrentTime = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingCurrentTime.setGeometry(QtCore.QRect(10, 200, 181, 16))
        self.LB_currentlyPlayingCurrentTime.setObjectName("LB_currentlyPlayingCurrentTime")
        self.ST_workerStack.addWidget(self.SC_sonosScreen)
        self.SC_weatherScreen = QtWidgets.QWidget()
        self.SC_weatherScreen.setObjectName("SC_weatherScreen")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.SC_weatherScreen)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 481, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.LB_weatherScreen = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LB_weatherScreen.setObjectName("LB_weatherScreen")
        self.horizontalLayout.addWidget(self.LB_weatherScreen)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LB_oldFreezer = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LB_oldFreezer.setObjectName("LB_oldFreezer")
        self.gridLayout.addWidget(self.LB_oldFreezer, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.LB_newFreezer = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LB_newFreezer.setObjectName("LB_newFreezer")
        self.gridLayout.addWidget(self.LB_newFreezer, 2, 1, 1, 1)
        self.LB_internalTemp = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_internalTemp.sizePolicy().hasHeightForWidth())
        self.LB_internalTemp.setSizePolicy(sizePolicy)
        self.LB_internalTemp.setObjectName("LB_internalTemp")
        self.gridLayout.addWidget(self.LB_internalTemp, 0, 1, 1, 1)
        self.LCD_newFreezer = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.LCD_newFreezer.setProperty("value", -16.2)
        self.LCD_newFreezer.setObjectName("LCD_newFreezer")
        self.gridLayout.addWidget(self.LCD_newFreezer, 2, 2, 1, 1)
        self.LCD_piTemp = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.LCD_piTemp.setSmallDecimalPoint(True)
        self.LCD_piTemp.setProperty("intValue", 40)
        self.LCD_piTemp.setObjectName("LCD_piTemp")
        self.gridLayout.addWidget(self.LCD_piTemp, 0, 2, 1, 1)
        self.LCD_oldFreezer = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.LCD_oldFreezer.setProperty("value", -15.5)
        self.LCD_oldFreezer.setObjectName("LCD_oldFreezer")
        self.gridLayout.addWidget(self.LCD_oldFreezer, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.ST_workerStack.addWidget(self.SC_weatherScreen)
        self.SC_log = QtWidgets.QWidget()
        self.SC_log.setObjectName("SC_log")
        self.TE_Debug = QtWidgets.QTextEdit(self.SC_log)
        self.TE_Debug.setGeometry(QtCore.QRect(10, 0, 461, 261))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.TE_Debug.setPalette(palette)
        self.TE_Debug.setObjectName("TE_Debug")
        self.ST_workerStack.addWidget(self.SC_log)
        self.SC_meteo = QtWidgets.QWidget()
        self.SC_meteo.setObjectName("SC_meteo")
        self.WD_browser = QtWidgets.QWidget(self.SC_meteo)
        self.WD_browser.setGeometry(QtCore.QRect(9, 9, 461, 251))
        self.WD_browser.setObjectName("WD_browser")
        self.WV_srfMeteo = QtWebKitWidgets.QWebView(self.WD_browser)
        self.WV_srfMeteo.setGeometry(QtCore.QRect(-1, -1, 461, 261))
        self.WV_srfMeteo.setUrl(QtCore.QUrl("http://m.srf.ch/meteo"))
        self.WV_srfMeteo.setObjectName("WV_srfMeteo")
        self.ST_workerStack.addWidget(self.SC_meteo)
        self.SC_sbb = QtWidgets.QWidget()
        self.SC_sbb.setObjectName("SC_sbb")
        self.gridLayoutWidget = QtWidgets.QWidget(self.SC_sbb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 461, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BT_hb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BT_hb.setFlat(True)
        self.BT_hb.setObjectName("BT_hb")
        self.gridLayout_2.addWidget(self.BT_hb, 0, 0, 1, 1)
        self.BT_wankdorf = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BT_wankdorf.setFlat(True)
        self.BT_wankdorf.setObjectName("BT_wankdorf")
        self.gridLayout_2.addWidget(self.BT_wankdorf, 0, 1, 1, 1)
        self.BT_breitsch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BT_breitsch.setFlat(True)
        self.BT_breitsch.setObjectName("BT_breitsch")
        self.gridLayout_2.addWidget(self.BT_breitsch, 0, 2, 1, 1)
        self.ST_workerStack.addWidget(self.SC_sbb)
        self.SC_hb = QtWidgets.QWidget()
        self.SC_hb.setObjectName("SC_hb")
        self.WD_hb = QtWidgets.QWidget(self.SC_hb)
        self.WD_hb.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.WD_hb.setObjectName("WD_hb")
        self.WV_sbbHB = QtWebKitWidgets.QWebView(self.WD_hb)
        self.WV_sbbHB.setGeometry(QtCore.QRect(0, 0, 461, 261))
        self.WV_sbbHB.setUrl(QtCore.QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml"))
        self.WV_sbbHB.setObjectName("WV_sbbHB")
        self.ST_workerStack.addWidget(self.SC_hb)
        self.SC_wankdorf = QtWidgets.QWidget()
        self.SC_wankdorf.setObjectName("SC_wankdorf")
        self.WD_wankdorf = QtWidgets.QWidget(self.SC_wankdorf)
        self.WD_wankdorf.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.WD_wankdorf.setObjectName("WD_wankdorf")
        self.WV_sbbWankdorf = QtWebKitWidgets.QWebView(self.WD_wankdorf)
        self.WV_sbbWankdorf.setGeometry(QtCore.QRect(0, 0, 461, 251))
        self.WV_sbbWankdorf.setUrl(QtCore.QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml"))
        self.WV_sbbWankdorf.setObjectName("WV_sbbWankdorf")
        self.ST_workerStack.addWidget(self.SC_wankdorf)
        self.SC_breitsch = QtWidgets.QWidget()
        self.SC_breitsch.setObjectName("SC_breitsch")
        self.WD_breitsch = QtWidgets.QWidget(self.SC_breitsch)
        self.WD_breitsch.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.WD_breitsch.setObjectName("WD_breitsch")
        self.WV_sbbBreitsch = QtWebKitWidgets.QWebView(self.WD_breitsch)
        self.WV_sbbBreitsch.setGeometry(QtCore.QRect(0, 0, 461, 251))
        self.WV_sbbBreitsch.setUrl(QtCore.QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml"))
        self.WV_sbbBreitsch.setObjectName("WV_sbbBreitsch")
        self.ST_workerStack.addWidget(self.SC_breitsch)
        MainWindowTarget.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowTarget)
        self.ST_workerStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowTarget)

    def retranslateUi(self, MainWindowTarget):
        _translate = QtCore.QCoreApplication.translate
        MainWindowTarget.setWindowTitle(_translate("MainWindowTarget", "SonosController"))
        self.BT_openHomeScreen.setText(_translate("MainWindowTarget", "HOME"))
        self.BT_openSonosScreen.setText(_translate("MainWindowTarget", "SONOS"))
        self.BT_openWeatherScreen.setText(_translate("MainWindowTarget", "WETTER"))
        self.BT_openMeteoScreen.setText(_translate("MainWindowTarget", "METEO"))
        self.BT_openSbbScreen.setText(_translate("MainWindowTarget", "SBB"))
        self.BT_openLogScreen.setText(_translate("MainWindowTarget", "LOG"))
        self.BT_sonosPlay.setText(_translate("MainWindowTarget", "Play"))
        self.BT_pause.setText(_translate("MainWindowTarget", "Pause"))
        self.BT_stop.setText(_translate("MainWindowTarget", "Stop"))
        self.BT_skip.setText(_translate("MainWindowTarget", "Next"))
        self.LB_currentlyPlayingTitle.setText(_translate("MainWindowTarget", "currently playing..."))
        self.BT_previous.setText(_translate("MainWindowTarget", "Previous"))
        self.LB_currentlyPlayingArtist.setText(_translate("MainWindowTarget", "Artist..."))
        self.BT_volumeUp.setText(_translate("MainWindowTarget", "+"))
        self.BT_volumeDown.setText(_translate("MainWindowTarget", "-"))
        self.LB_currentlyPlayingPosition.setText(_translate("MainWindowTarget", "currently playing..."))
        self.LB_currentlyPlayingTotal.setText(_translate("MainWindowTarget", "currently playing..."))
        self.LB_currentlyPlayingCurrentTime.setText(_translate("MainWindowTarget", "currently playing..."))
        self.LB_weatherScreen.setText(_translate("MainWindowTarget", "This is the weather screen"))
        self.LB_oldFreezer.setText(_translate("MainWindowTarget", "Temp alter Gefrierschrank"))
        self.LB_newFreezer.setText(_translate("MainWindowTarget", "Temp neuer Gefrierschrank"))
        self.LB_internalTemp.setText(_translate("MainWindowTarget", "internal Temp"))
        self.BT_hb.setText(_translate("MainWindowTarget", "Bahnhof"))
        self.BT_wankdorf.setText(_translate("MainWindowTarget", "Wankdorf"))
        self.BT_breitsch.setText(_translate("MainWindowTarget", "Breitsch"))

from PyQt5 import QtWebKitWidgets
