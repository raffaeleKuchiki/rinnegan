# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookmarks.ui'
#
# Created: Fri Jan 30 18:13:38 2015
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

class Ui_bookmarks(object):
    def setupUi(self, bookmarks):
        bookmarks.setObjectName(_fromUtf8("bookmarks"))
        bookmarks.resize(455, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ico/rinnegan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bookmarks.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(bookmarks)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(bookmarks)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(bookmarks)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("cellDoubleClicked(int,int)")), bookmarks.bookmarks_open)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), bookmarks.bookmarks_contextMenu)
        QtCore.QMetaObject.connectSlotsByName(bookmarks)

    def retranslateUi(self, bookmarks):
        bookmarks.setWindowTitle(_translate("bookmarks", "Bookmarks", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("bookmarks", "name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("bookmarks", "url", None))

