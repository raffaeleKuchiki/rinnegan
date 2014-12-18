from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
sys.path.append('ui/')
from chronos import *
from sqlite_lib import *

class Chrono(QWidget,Ui_chronos):
  def __init__(self):
    super(Chrono,self).__init__()
    self.setupUi(self)
    self.chrono_query()
    
  def chrono_query(self):
    data = Database("data/WebpageIcons.db")
    echo = data.db_select("SELECT PageURL.url, IconInfo.url FROM PageURL JOIN IconInfo ON PageURL.iconID=IconInfo.iconID")
    i=0
    while i<len(echo):
      text = str(echo[i][0])
      icon = QIcon(QPixmap(str(echo[i][1])))
      HIcon = QTableWidgetItem("")
      HIcon.setIcon(icon)
      HIcon.setTextAlignment(QtCore.Qt.AlignVCenter)
      
      self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
      self.tableWidget.setItem(i,1,QTableWidgetItem(text))
      self.tableWidget.setItem(i,0,HIcon)
      i += 1
    data.db_close()