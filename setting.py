from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, json
sys.path.append("/ui")
from xml.etree.ElementTree import *
from ui_setting import *

class Setting(QWidget,Ui_setting):
	def __init__(self,parent):
		super(Setting,self).__init__()
		self.setupUi(self)
		self.parent = parent
		self.update()
		
	def update(self):
		f = open("data/home.json","r")
		data = json.load(f)
		self.lineEdit.setText(QString(data["home"]))
		f.close()
	
	def setting_url_from_tab(self): 
		widget = self.parent.tabWidget.currentWidget()
		url = widget.qwebview.url().toString()
		self.lineEdit.setText(url)
		
	def setting_save(self):
		url = self.lineEdit.text()
		f = open("data/home.json","r+")
		data = json.load(f)
		
		data["home"] = str(url)
		
		f.seek(0)
		f.write(json.dumps(data,indent = 9))
		f.truncate()
		f.close()
		
		self.update()