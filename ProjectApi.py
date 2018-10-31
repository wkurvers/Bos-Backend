from flask import jsonify

from Database import Project
import hashlib
from Persister import Persister
import os
import datetime

persister = Persister()

class ProjectApi():
	def __init__(self):
		print("creating projectApi")

	def getProjectById(self,id):
		return persister.getProjectById(id)

	def addProject(self, title, description, thumbnail, creator, beginDate, endDate):
		if persister.checkUserExists(creator):
			path = "C:/Users/Jelmer/Bos-Backend/thumbnails/"
			mediaPath = path + title + "Base64.txt"
			mediaFile = open(mediaPath, "w+")
			mediaFile.write(thumbnail)
			mediaFile.close()
	
			currentDate = datetime.datetime.now()
	
			projectObject = Project ( 
										title=title,
								  		description=description,
								  		thumbnail=mediaPath,
								  		creator=creator,
								  		beginDate=beginDate,
								  		endDate=endDate,
										createdAt=currentDate,
										likes=0
									)
			return persister.storeObject(projectObject)
		return False

    # def addLike(self, id):
    #     Persister.addLike(id)

    # def removeLike(self, id):
    #     Persister.removeLike(id)

    # def totalLikes(self, id):
    #     return jsonify({"totalLikes": Persister.totalLikes(id)})
