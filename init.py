from PyQt4.QtGui import QApplication
import sys,os,errno
from browser import *

if __name__=="__main__":
	#change name process
	if sys.platform == 'linux2':
		import ctypes
		libc = ctypes.cdll.LoadLibrary('libc.so.6')
		libc.prctl(15, "Rinnegan", 0, 0, 0)
	try:
		os.makedirs('data/')
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir('data/'):
			pass
		else:
			raise
	app = QApplication(sys.argv)
	app.setApplicationName("Rinnegan")
	r = Browser()
	sys.exit(app.exec_())