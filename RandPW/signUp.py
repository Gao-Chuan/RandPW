from InterfaceLayer import aes, sha256
import sqlite3
import os
import codecs

class signUpWin(object):
	"""docstring for signUpWin"""
	username = None
	key = None
	sault = None
	status = 0

	def __init__(self, username, key):
		super(signUpWin, self).__init__()
		self.sault = str(os.urandom(16))[2:-1]
		self.username = str(codecs.encode(sha256(username), 'hex'))[2:-1]
		self.key = str(codecs.encode(sha256(key + self.sault), 'hex'))[2:-1]
		self.status = self.DBoperation()

	def DBoperation(self):
		try:
			userInfo_Db = sqlite3.connect('C:/RandPwData/userInfo.db')
		except sqlite3.OperationalError as e:
			os.mkdir('C:/RandPwData/')
			userInfo_Db = sqlite3.connect('C:/RandPwData/userInfo.db')

		db = userInfo_Db.cursor()

		try:
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		except sqlite3.OperationalError as e:
			db.execute("create table userInfo (username text unique, key text, sault text)")
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		except sqlite3.IntegrityError as e:
			return 0
		except:
			return -1

		userInfo_Db.commit()
		db.close()
		userInfo_Db.close()

		users = sqlite3.connect('C:/RandPwData/users.db')
		db = users.cursor()
		db.execute('create table "' + self.username + '" (site text unique, sault text, userDefined integer)')
		return 1


class signUpLinux(object):
	"""docstring for signUpLinux"""
	username = None
	key = None
	sault = None
	status = 0

	def __init__(self, username, key):
		super(signUpLinux, self).__init__()
		self.sault = str(os.urandom(16))[2:-1]
		self.username = str(codecs.encode(sha256(username), 'hex'))[2:-1]
		self.key = str(codecs.encode(sha256(key + self.sault), 'hex'))[2:-1]
		self.status = self.DBoperation()

	def DBoperation(self):
		try:
			userInfo_Db = sqlite3.connect('~/RandPwData/userInfo.db')
		except sqlite3.OperationalError as e:
			os.mkdir('~/RandPwData/')
			userInfo_Db = sqlite3.connect('~/RandPwData/userInfo.db')

		db = userInfo_Db.cursor()

		try:
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		except sqlite3.OperationalError as e:
			db.execute("create table userInfo (username text unique, key text, sault text)")
			db.execute("insert into userInfo values (?,?,?)", (self.username, self.key, self.sault))
		except sqlite3.IntegrityError as e:
			return 0
		except:
			return -1

		userInfo_Db.commit()
		db.close()
		userInfo_Db.close()

		users = sqlite3.connect('~/RandPwData/users.db')
		db = users.cursor()
		db.execute('create table "' + self.username + '" (site text unique, sault text, userDefined integer)')

		return 1


#test code
# info = signUpWin("name", "key")

# userInfo_Db = sqlite3.connect('C:/RandPwData/userInfo.db')
# db = userInfo_Db.cursor()
# db.execute('select * from userInfo')
# print(db.fetchall())