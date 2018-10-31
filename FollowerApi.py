from Database import Follower
import hashlib
from Persister import Persister

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

	def addFollower(self, project, user):
		if not persister.getProjectById(project) == False and not persister.getUserById(user) == False:
			if persister.checkFollowerExists(user, project):
				followerObject = Follower( user=user, project=project)
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
		index = 0
		for entry in followersArray:
			follower = {}
			follower['id'] = entry.id
			follower['project'] = entry.project
			follower['user'] = entry.user
			returnData[index] = follower
			index += 1
		return returnData

