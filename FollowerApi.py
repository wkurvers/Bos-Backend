from Database import Follower
import hashlib
from Persister import Persister
import requests
import json

persister = Persister()

class FollowerApi():
	def __init__(self):
		print("creating followerApi")

	def getFollowerById(self, id):
		return persister.getFollowerById(id)

	def getFollowerByContext(self, user, project):
		return persister.getFollowerByContext(id)

	def getFollowersByProject(self,project):
		return persister.getFollowersByProject(project)

	def addFollower(self, project, user, deviceId):
		if not persister.getProjectById(project) == False and not persister.getUserById(user) == False:
			if not persister.checkFollowerExists(user, project):
				followerObject = Follower( user=user, project=project, deviceId=deviceId)
				return persister.storeObject(followerObject)
		return False

	def removeFollower(self, id):
		follower = self.getFollowerById(id)
		if follower != False:
			return persister.deleteObject(follower) #True or False depening on succes
		return False #1 or more necessary fields were empty or user did not exist

	def getFollowersForProject(self,project):
		followersArray = persister.getFollowersByProject(project)
		returnData = {}
		for entry in followersArray:
			follower = {}
			follower['id'] = entry.id
			follower['project'] = entry.project
			follower['user'] = entry.user
			follower['deviceId'] = entry.deviceId
			returnData[entry.id] = follower
		return returnData

	def pushFollowers(self, project):
		followers = self.getFollowersForProject(project)
		deviceIds = [];
		for entry in followers:
			user = followers[entry]
			deviceIds.append(user['deviceId'])

		apiKey = "Y2M0Y2JmNjEtOGM1NS00YmUxLTk0ZWQtNWJjZjY0NjVhYWVi"
		appId = "40e57605-3c79-454d-a577-c07aea4a7991"
		header = {"Content-Type": "application/json; charset=utf-8",
		        "Authorization": "Basic " + apiKey}
		print(deviceIds)
		payload = {"app_id": appId,
		       		"include_player_ids": deviceIds,
		       		"contents": {"en": "Nieuws van het project"},
		       		"headings": {"en": "nieuws"}}
		
		req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
		return True

