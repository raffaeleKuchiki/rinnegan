from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append('ui/')
from ui_bookmarks import *
from sqlite_lib import *

class Bookmarks(QWidget,Ui_bookmarks):
	def __init__(self,parent):
		super(Bookmarks,self).__init__()
		self.parent = parent
		self.setupUi(self)
		self.bookmarks_query()
		
	def bookmarks_open(self,row,column):
		url = self.tableWidget.item(row,1)
		print url.text()
		self.parent.newTab(url.text())
		
	def bookmarks_query(self):
		self.data = Database("data/bookmarks.db")
		echo = self.data.db_select("SELECT * FROM bookmarks")
		print len(echo)
		i=0
		while i<len(echo):
			name = str(echo[i][0])
			url = str(echo[i][1])
			self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
			self.tableWidget.setItem(i,0,QTableWidgetItem(name))
			self.tableWidget.setItem(i,1,QTableWidgetItem(url))
			i+=1