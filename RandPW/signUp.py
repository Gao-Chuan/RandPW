from InterfaceLayer import aes, sha256
import sqlite3
import os
import codecs


class signUpWin(object):
	"""docstring for signUpWin"""
	username = None
	key = None
	sault = None

	def __init__(self, username, key):
		super(signUpWin, self).__init__()
		self.sault = str(os.urandom(16))
		self.username = codecs.encode(sha256(username + self.sault), 'hex')
		self.key = codecs.encode(sha256(key + self.sault), 'hex')
		self.DBoperation()

	def DBoperation(self):
		try:
			userInfo_Db = sqlite3.connect('C:/RandPwData/userInfo.db')
		except Exception as e:
			os.mkdir('C:/RandPwData/')
			userInfo_Db = sqlite3.connect('C:/RandPwData/userInfo.db')

		db = userInfo_Db.cursor()

		try:
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		except Exception as e:
			db.execute("create table userInfo (username text unique, key text, sault text)")
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		userInfo_Db.commit()
		db.close()
		userInfo_Db.close()




class signUpLinux(object):
	"""docstring for signUpLinux"""
	username = None
	key = None
	sault = None

	def __init__(self, username, key):
		super(signUpLinux, self).__init__()
		self.sault = str(os.urandom(16))
		self.username = codecs.encode(sha256(username + self.sault), 'hex')
		self.key = codecs.encode(sha256(key + self.sault), 'hex')
		self.DBoperation()

	def DBoperation(self):
		try:
			userInfo_Db = sqlite3.connect('~/RandPwData/userInfo.db')
		except Exception as e:
			os.mkdir('C:/RandPwData/')
			userInfo_Db = sqlite3.connect('~/RandPwData/userInfo.db')

		db = userInfo_Db.cursor()

		try:
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		except Exception as e:
			db.execute("create table userInfo (username text unique, key text, sault text)")
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		userInfo_Db.commit()
		db.close()
		userInfo_Db.close()



#test code
# info = signUpWin("name", "key")

# userInfo_Db = sqlite3.connect('C:/RandPwData/userInfo.db')
# db = userInfo_Db.cursor()
# db.execute('select * from userInfo')
# print(db.fetchall())