from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append('ui/')
from window import *
from view import *
from chrono import *

class Browser(QMainWindow,Ui_MainWindow):
  def __init__(self):
    super(Browser, self).__init__()
    self.setupUi(self)
    self.newTab()
    self.show()
    self.tabWidget.setTabsClosable(False)
    
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
    self.dialog = Chrono(self)
    self.dialog.show()
    self.dialog.isVisible()