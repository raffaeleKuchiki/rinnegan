from PyQt4.QtGui import QApplication
import sys,os,errno
from browser import *

if __name__=="__main__":
	try:
		os.makedirs('data/')
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir('data/'):
			pass
		else:
			raise
	app = QApplication(sys.argv)
	r = Browser()
	sys.exit(app.exec_())