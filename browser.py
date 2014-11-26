#!/usr/bin/python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append('ui/')
from window import *
from view import *

class Browser(QMainWindow,Ui_MainWindow):
  def __init__(self):
    super(Browser, self).__init__()
    self.setupUi(self)
    self.newTab()
    self.show()
    self.tabWidget.setTabsClosable(False)
    
  def newTab(self):
    self.tabWidget.addTab(View(self),QString(""))
    self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)
    if self.tabWidget.count()>1:
      self.tabWidget.setTabsClosable(True)
      
  def tabClose(self,index):
    widget = self.tabWidget.widget(index)
    widget.destroy()
    self.tabWidget.removeTab(index)
    if self.tabWidget.count()<=1:
      self.tabWidget.setTabsClosable(False)
      
  def tabSelection(self,index):
    widget = self.tabWidget.widget(index)
    self.tabWidget.setTabText(index,widget.qwebview.title())
    self.tabWidget.setTabIcon(index,widget.qwebview.icon())
      
  def tabTitle(self,title):
    index = self.tabWidget.currentIndex()
    self.tabWidget.setTabText(index,QString(title))
    
  def tabIcon(self,icon):
    index = self.tabWidget.currentIndex()
    self.tabWidget.setTabIcon(index,QIcon(icon))