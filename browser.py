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
		self.chro = Database("data/WebpageIcons.db")
		self.book = Database("data/bookmarks.db")
		try:
			self.book.db_iniection("CREATE TABLE bookmarks (id integer PRIMARY KEY, name text, url text)")
		except:
			print "already exist"
    
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