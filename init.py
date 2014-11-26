#!/usr/bin/python

from PyQt4.QtGui import QApplication
from browser import *

if __name__=="__main__":
  app = QApplication(sys.argv)
  r = Browser()
  sys.exit(app.exec_())