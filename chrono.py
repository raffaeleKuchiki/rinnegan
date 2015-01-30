from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append('ui/')
from ui_chronos import *
from sqlite_lib import *

class Chrono(QWidget,Ui_chronos):
	def __init__(self,parent):
		super(Chrono,self).__init__()
		self.parent = parent
		self.setupUi(self)
		self.chrono_query()
	
	def chrono_query(self):
		echo = self.parent.data.db_select("SELECT ico, url, date FROM chronos ORDER BY datetime(date)")
		i=0
		while i<len(echo):
			self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
			ico = str(echo[i][0])
			url = str(echo[i][1])
			date = str(echo[i][2])
			#prova = QTableWidgetItem()
			#prova.setIcon(pic)
			self.tableWidget.setItem(i,0,QTableWidgetItem(ico))
			self.tableWidget.setItem(i,1,QTableWidgetItem(url))
			self.tableWidget.setItem(i,2,QTableWidgetItem(date))
			i += 1
	
	def chrono_contextMenu(self,point):
		menu = QtGui.QMenu()
		action1 = menu.addAction(QIcon("ico/delete.png"),"Delete All Same Url")
		action2 = menu.addAction(QIcon("ico/clean.png"),"Clean History")
		QObject.connect(action1,SIGNAL("triggered()"),self.chrono_delete)
		QObject.connect(action2,SIGNAL("triggered()"),self.chrono_clearHistory)
		menu.exec_(self.mapToGlobal(point))
	
	def chrono_delete(self):
		index = self.tableWidget.currentRow()
		url = self.tableWidget.item(index,1).text()
		self.parent.data.db_iniection("DELETE FROM chronos WHERE url='"+str(url)+"'")
		self.chrono_clean_view()
		self.chrono_query()
	
	def chrono_clearHistory(self):
		self.parent.data.db_iniection("DELETE FROM chronos")
		print ("history cleaned")
		self.chrono_clean_view()
		self.chrono_query()
	
	def chrono_clean_view(self):
		count = self.tableWidget.rowCount()
		i=count-1
		while 0<=i:
			self.tableWidget.removeRow(i)
			i -= 1
	
	def chrono_open(self,row,column):
		url = self.tableWidget.item(row,1)
		self.parent.newTab(url.text())
	