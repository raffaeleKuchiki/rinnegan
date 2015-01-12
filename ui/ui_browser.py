# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Mon Jan 12 20:59:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_browser(object):
    def setupUi(self, browser):
        browser.setObjectName(_fromUtf8("browser"))
        browser.resize(800, 632)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ico/rinnegan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        browser.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(browser)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        browser.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(browser)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        browser.setMenuBar(self.menuBar)
        self.actionNew_tab = QtGui.QAction(browser)
        self.actionNew_tab.setObjectName(_fromUtf8("actionNew_tab"))
        self.actionChronos = QtGui.QAction(browser)
        self.actionChronos.setObjectName(_fromUtf8("actionChronos"))
        self.actionBookmarks = QtGui.QAction(browser)
        self.actionBookmarks.setObjectName(_fromUtf8("actionBookmarks"))
        self.menuFile.addAction(self.actionNew_tab)
        self.menuFile.addAction(self.actionChronos)
        self.menuFile.addAction(self.actionBookmarks)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(browser)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("tabCloseRequested(int)")), browser.tabClose)
        QtCore.QObject.connect(self.actionNew_tab, QtCore.SIGNAL(_fromUtf8("triggered()")), browser.newTab)
        QtCore.QObject.connect(self.actionChronos, QtCore.SIGNAL(_fromUtf8("triggered()")), browser.chrono)
        QtCore.QObject.connect(self.actionBookmarks, QtCore.SIGNAL(_fromUtf8("triggered()")), browser.bookmarks)
        QtCore.QMetaObject.connectSlotsByName(browser)

    def retranslateUi(self, browser):
        browser.setWindowTitle(_translate("browser", "Rinnegan", None))
        self.menuFile.setTitle(_translate("browser", "file", None))
        self.actionNew_tab.setText(_translate("browser", "new tab", None))
        self.actionChronos.setText(_translate("browser", "chronos", None))
        self.actionBookmarks.setText(_translate("browser", "bookmarks", None))

