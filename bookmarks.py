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
		print (url.text())
		self.parent.newTab(url.text())
		
	def bookmarks_query(self):
		echo = self.parent.date.db_select("SELECT * FROM bookmarks")
		i=0
		while i<len(echo):
			name = str(echo[i][1])
			url = str(echo[i][2])
			self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
			self.tableWidget.setItem(i,0,QTableWidgetItem(name))
			self.tableWidget.setItem(i,1,QTableWidgetItem(url))
			i+=1
	
	def bookmarks_contextMenu(self,point):
		menu = QtGui.QMenu()
		action1 = menu.addAction(QIcon("ico/delete.png"),"Delete")
		action2 = menu.addAction(QIcon("ico/rename.png"),"Rename")
		QObject.connect(action1,SIGNAL("triggered()"),self.bookmarks_delete)
		QObject.connect(action2,SIGNAL("triggered()"),self.bookmarks_rename)
		menu.exec_(self.mapToGlobal(point))
	
	def bookmarks_delete(self):
		index = self.tableWidget.currentRow()
		url = self.tableWidget.item(index,1).text()
		self.parent.date.db_iniection("DELETE FROM bookmarks WHERE url='"+str(url)+"'")
		self.bookmarks_clean_view()
		self.bookmarks_query()
	
	def bookmarks_rename(self):
		index = self.tableWidget.currentRow()
		url = self.tableWidget.item(index,1).text()
		old_name = self.tableWidget.item(index,0).text()
		new_name, ok = QInputDialog.getText(self.parent,'Rename Bookmark','Enter Bookmark Name: ',QLineEdit.Normal,str(old_name))
		if ok==True:
			self.parent.date.db_iniection("UPDATE bookmarks SET name='"+str(new_name)+"' WHERE url='"+str(url)+"'")
		self.bookmarks_clean_view()
		self.bookmarks_query()
	
	def bookmarks_clean_view(self):
		count = self.tableWidget.rowCount()
		i=count-1
		while 0<=i:
			self.tableWidget.removeRow(i)
			i -= 1