# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chronos.ui'
#
# Created: Fri Jan  9 16:32:24 2015
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
        chronos.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ico/rinnegan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        chronos.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(chronos)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(chronos)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(chronos)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(chronos)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(chronos)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), chronos.chrono_clearHistory)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), chronos.chrono_open)
        QtCore.QMetaObject.connectSlotsByName(chronos)

    def retranslateUi(self, chronos):
        chronos.setWindowTitle(_translate("chronos", "Chronos", None))
        self.pushButton.setText(_translate("chronos", "Open", None))
        self.pushButton_2.setText(_translate("chronos", "clear history", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("chronos", "ico", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("chronos", "url", None))

