from Database import Media
import hashlib
from Persister import Persister
import os

persister = Persister()

class MediaApi():
	def __init__(self):
		print("creating mediaApi")

	def getMediaById(self, id):
		return persister.getMediaById(id) #User object

	def storeMedia(self, project, name, media):
		path = "C:/Users/Jelmer/Bos-Backend/media/"
		mediaPath = path + name + "Base64.txt"
		mediaFile = open(mediaPath, "w+")
		mediaFile.write(media)
		mediaFile.close()

		mediaObject = Media ( 
								project=project,
							  	name=name,
							  	mediaPath=mediaPath
							)
		if not persister.storeObject(mediaObject):
			os.remove(mediaPath)
			return False
		return True

	def removeMedia(self, id):
		media = self.getMediaById(id)
		if media != False:
			os.remove(media.mediaPath)
			return persister.deleteObject(media) #True or False depening on succes
		return False #1 or more necessary fields were empty or user did not exist
