from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append("/ui")
from xml.etree.ElementTree import *
from ui_setting import *

class Setting(QWidget,Ui_setting):
	def __init__(self,parent):
		super(Setting,self).__init__()
		self.setupUi(self)
		self.parent = parent
		self.data = ElementTree(file = "data/home.xml")
		self.update()
		
	def update(self):
		url = self.data.find("home/url").text
		self.lineEdit.setText(QString(url))
	
	def setting_url_from_tab(self):
		widget = self.parent.tabWidget.currentWidget()
		url = widget.qwebview.url().toString()
		self.lineEdit.setText(url)
		
	def setting_save(self):
		url = self.lineEdit.text()
		self.data.find("home/url").text = str(url)
		self.data.write("data/home.xml")
		self.update()