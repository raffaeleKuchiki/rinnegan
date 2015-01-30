import sqlite3
import sys

class Database():
	def __init__(self,name):
		self.iniection_count=1
		self.name = name
		self.db_fileName()
		try:
			self.connection = sqlite3.connect(self.name)
			print ("connection created")
			self.db_cursor()
		except:
			print ("connection failed")
    
	def db_fileName(self):
		count = len(self.name)
		i=0
		temp = ""
		while i < count:
			char = self.name[i]
			if char!=".":
				temp += char
			else:
				i = count
				self.name = temp + ".db"
			i += 1

	def db_cursor(self):
		try:
			self.cursor = self.connection.cursor()
			print ("cursor created")
		except:
			print ("cursor failed")

	def db_iniection(self,query):
		self.cursor.execute(query)
		self.connection.commit()
		print ("iniection number " , self.iniection_count)
		self.iniection_count += 1
    
	def db_select(self,query):
		self.cursor.execute(query)
		array = self.cursor.fetchall()
		return array
    
	def db_close(self):
		self.connection.close()
		print ("connection closed")