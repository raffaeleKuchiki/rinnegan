import os
from distutils.core import setup

def read(faname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
	name="Rinnegan",
	version="1.0.0",
	author="Raffaele Francesco Mancino",
	description="Simple Browser web",
	
)