from Database import Project
import hashlib
from Persister import Persister
import os

persister = Persister()

class ProjectApi():
	def __init__(self):
		print("creating projectApi")

	def getProjectById(self,id):
		return persister.getProjectById(id)

	def addProject(self, title, description, thumbnail, creator, beginDate, endDate, createdAt):
		path = "C:/Users/Jelmer/Bos-Backend/thumbnails/"
		mediaPath = path + name + "Base64.txt"
		mediaFile = open(mediaPath, "w+")
		mediaFile.write(thumbnail)
		mediaFile.close()

		projectObject = Project ( 
								title=title,
							  	description=description,
							  	thumbnail=mediaPath,
							  	creator=creator,
							  	beginDate=beginDate,
							  	endDate=endDate
							)