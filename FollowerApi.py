from Database import Follower
import hashlib
from Persister import Persister

persister = Persister()

class FollowerApi():
	def __init__(self):
		print("creating followerApi")

	def getFollowerById(self, id):
		return persister.getFollowerById(id)

	def addFollower(self, project, user):
		if not persister.getProjectById(project) == False and not persister.getUserById(user) == False:
			if persister.checkFollowerExists(user, project):
				followerObject = Follower( user=user, project=project)
				return persister.storeObject(followerObject)
		return False
