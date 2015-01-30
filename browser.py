from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, os
sys.path.append('ui/')
from lxml import etree
from ui_browser import *
from view import *
from chrono import *
from bookmarks import *
from setting import *
from sqlite_lib import *

class Browser(QMainWindow,Ui_browser):
	def __init__(self):
		super(Browser, self).__init__()
		self.setupUi(self)
		self.show()
		self.tabWidget.setTabsClosable(False)
		self.data = Database("data/browser_data.db")
		
		self.data.db_iniection("CREATE TABLE IF NOT EXISTS bookmarks (id integer PRIMARY KEY, name text, url text)")
		self.data.db_iniection("CREATE TABLE IF NOT EXISTS chronos (id integer PRIMARY KEY, ico text, url text, date datetime default CURRENT_TIMESTAMP)")
		self.xml_home_file()
		
		self.newTab()
    
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
		
	def setting(self):
		self.s = Setting(self)
		self.s.show()
		self.s.isVisible()
	
	def xml_home_file(self):
		test = os.path.exists('data/home.xml')
		print test
		if not test:
			root = etree.Element('data')
			subroot = etree.Element('home')
			child = etree.Element('url')
			child.text = "http://start.ubuntu.com"
			subroot.append(child)
			root.append(subroot)
			
			s = etree.tostring(root,pretty_print=True)
			output = open('data/home.xml','w')
			output.write(s)
			output.close()