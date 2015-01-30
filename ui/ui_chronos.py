# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chronos.ui'
#
# Created: Fri Jan 30 13:49:29 2015
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

class Ui_chronos(object):
    def setupUi(self, chronos):
        chronos.setObjectName(_fromUtf8("chronos"))
        chronos.resize(471, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ico/rinnegan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        chronos.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(chronos)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(chronos)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(chronos)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("cellDoubleClicked(int,int)")), chronos.chrono_open)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), chronos.chrono_contextMenu)
        QtCore.QMetaObject.connectSlotsByName(chronos)

    def retranslateUi(self, chronos):
        chronos.setWindowTitle(_translate("chronos", "Chronos", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("chronos", "ico", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("chronos", "url", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("chronos", "date", None))

