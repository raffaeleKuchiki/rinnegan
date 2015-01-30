from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append('ui/')
from ui_browser import *
from view import *
from chrono import *
from bookmarks import *
from sqlite_lib import *

class Browser(QMainWindow,Ui_browser):
	def __init__(self):
		super(Browser, self).__init__()
		self.setupUi(self)
		self.newTab()
		self.show()
		self.tabWidget.setTabsClosable(False)
		self.data = Database("data/browser_data.db")
		
		self.data.db_iniection("CREATE TABLE IF NOT EXIST bookmarks (id integer PRIMARY KEY, name text, url text)")
		self.data.db_iniection("CREATE TABLE IF NOT EXIST chronos (id integer PRIMARY KEY, ico text, url text, date datetime default CURRENT_TIMESTAMP)")
    
	def newTab(self,url=""):
		self.tabWidget.addTab(View(self,url),QString(""))
		self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)
		if self.tabWidget.count()>1:
			self.tabWidget.setTabsClosable(True)
		self.tabWindowIndex()
      
	def tabClose(self,index):
		widget = self.tabWidget.widget(index)
		widget.destroy()
		self.tabWidget.removeTab(index)
		if self.tabWidget.count()<=1:
			self.tabWidget.setTabsClosable(False)
		self.tabWindowIndex()
      
	def tabWindowIndex(self):
		count = self.tabWidget.count()
		for x in range(0,count):
			widget = self.tabWidget.widget(x)
			widget.index = x
      
	def tabTitle(self,title,index):
		self.tabWidget.setTabText(index,QString(title))
    
	def tabIcon(self,icon,index):
		self.tabWidget.setTabIcon(index,QIcon(icon))
    
	def chrono(self):
		self.c = Chrono(self)
		self.c.show()
		self.c.isVisible()
	
	def bookmarks(self):
		self.b = Bookmarks(self)
		self.b.show()
		self.b.isVisible()