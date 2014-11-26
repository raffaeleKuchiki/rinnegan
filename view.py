#!/usr/bin/python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import sys
sys.path.append('ui/')
from page import * 

class View(QWidget,Ui_page):
  def __init__(self,parent):
    super(View,self).__init__()
    self.parent = parent
    self.setupUi(self)
    self.qwebview.setUrl(QUrl('http://start.ubuntu.com'))
    QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
    QWebSettings.setIconDatabasePath('data/')
 
  def viewLoading(self,value):
   self.progressBar.setValue(value)
   if value==100:
     self.progressBar.setValue(0)
     
  def viewReload(self):
    self.qwebview.reload()
    
  def viewStop(self):
    self.qwebview.stop()
    
  def viewForward(self):
    self.qwebview.forward()
  
  def viewBack(self):
    self.qwebview.back()
    
  def viewHome(self):
    self.qwebview.setUrl(QUrl('http://start.ubuntu.com'))
    
  def viewTitle(self,title):
    self.parent.tabTitle(title)
    
  def viewIcon(self):
    self.parent.tabIcon(self.qwebview.icon())