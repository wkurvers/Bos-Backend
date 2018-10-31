from Database import Event
import hashlib
from Persister import Persister
import datetime

persister = Persister()

class EventApi():
	def __init__(self):
		print("creating eventApi")

	def addEvent(self, title, description, project, beginDate, endDate):
		if persister.checkProjectExists(project):
			currentDate = datetime.datetime.now()
			eventObject = Event( 	title=title,
									description=description,
									project=project,
									beginDate=beginDate,
									endDate=endDate,
									createdAt=currentDate)
			return persister.storeObject(eventObject)
		return False

	def getAllEvents(self):
		eventsArray = perister.getAllEvents()
		returnData = {}
		for entry in eventsArray:
			event = {}
			event['id'] = entry.id
			event['title'] = entry.title
			event['description'] = entry.description
			event['project'] = entry.project
			event['beginDate'] = entry.beginDate
			event['endDate'] = entry.endDate
			event['createdAt'] = entry.createdAt
			returnData[entry.id] = event
		return returnData
