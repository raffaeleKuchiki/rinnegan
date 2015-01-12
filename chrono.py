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
		echo = self.parent.chro.db_select("SELECT IconInfo.url, PageURL.url FROM PageURL JOIN IconInfo ON PageURL.iconID=IconInfo.iconID")
		i=0
		while i<len(echo):
			text = str(echo[i][1])
			self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
			pic = QIcon(str(echo[i][0]))
			prova = QTableWidgetItem()
			prova.setIcon(pic)
			self.tableWidget.setItem(i,0,prova)
			self.tableWidget.setItem(i,1,QTableWidgetItem(text))
			i += 1
	
	def chrono_clearHistory(self):
		self.parent.chro.db_iniection("DELETE FROM PageURL")
		print "history cleaned"
		self.close()
	
	def chrono_open(self,row,column):
		url = self.tableWidget.item(row,1)
		self.parent.newTab(url.text())