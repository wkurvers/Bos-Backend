from Database import User
import hashlib
from Persister import Persister

persister = Persister()

class UserApi():
	def __init__(self):
		print("creating userapi")

	def getUserById(self, id):
		return persister.getUserById(id) #User object

	def getUserByEmail(self, email):
		return persister.getUserByEmail(email) #User object

	def saveUser(self, name, email, password,
				 locationCity, profilePhoto, description , organisation):
		arrayOfData = [name, email, password, locationCity, profilePhoto, description , organisation]
		if self.checkData(arrayOfData):
			hashedPw = hashlib.sha256(password.encode('utf-8')).hexdigest()
			path = "C:/Users/Jelmer/Bos-Backend/profilephoto's/"
			mediaPath = path + name + "Base64.txt"
			mediaFile = open(mediaPath, "w+")
			mediaFile.write(profilePhoto)
			mediaFile.close()
			userObject = User(	name=name.lower(), 
								email=email.lower(), 
								password=hashedPw, 
								authenticated=False,
								locationCity=locationCity,
								profilePhoto=mediaPath,
								description=description,
								organisation=organisation)
			return persister.storeObject(userObject) #True or False depening on succes
		return False #1 or more necessary fields were empty

	def removeUser(self, id):
		user = self.getUserById(id)
		if user != False:
			return persister.deleteObject(user) #True or False depening on succes
		return False #1 or more necessary fields were empty or user did not exist

	def loginUser(self, email, password):
		arrayOfData = [email, password]
		if self.checkData(arrayOfData):
			sendPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
			user = self.getUserByEmail(email)
			if user != False:
				if sendPassword == user.password:
					return persister.setAuthenticated(email) #True or False depening on succes
		return False #1 or more necessary fields were empty or user did not exist

	def logoutUser(self, email):
		arrayOfData = [email]
		if self.checkData(arrayOfData):
			user = self.getUserByEmail(email)
			if user != False:
				return persister.setNotAuthenticated(email) #True or False depening on succes
		return False #email field was empty or user did not exist

	def checkData(self, arrayOfData):
		for data in arrayOfData:	#check array of data to make sure no None values or empty strings are send, works only if all variables in array are strings
			if data == '' or data == None:
				return False
		return True
