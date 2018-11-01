from Database import NecessitiesRequest
import hashlib
from Persister import Persister
import datetime

persister = Persister()

class NecessitiesRequestApi():
	def __init__(self):
		print("creating necessitiesRequestApi")

	def makeRequest(self, owner, title, description, necessity):
		if persister.checkUserExists(owner):
			requestObject = NecessitiesRequest(	owner=owner,
												title=title,
												description=description,
												necessity=necessity,
												createdAt=datetime.datetime.now())
			return persister.storeObject(requestObject)
		return False

	def getRequestById(self, id):
		dbObject = persister.getRequestById(id)
		if dbObject != False:
			request = {
				"id": dbObject.id,
				"owner": dbObject.owner,
				"title": dbObject.title,
				"description": dbObject.description,
				"necessity": dbObject.necessity,
				"createdAt": dbObject.createdAt
			}
			return request
		return False

	def getAllRequests(self):
		requests = persister.getAllRequests()
		returnData = {}
		for entry in requests:
			request = {}
			request['id'] = entry.id
			request['owner'] = entry.owner
			request['title'] = entry.title
			request['description'] = entry.description
			request['necessity'] = entry.necessity
			request['createdAt'] = entry.createdAt
			returnData[entry.id] = request
		return returnData