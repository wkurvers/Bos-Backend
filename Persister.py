import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker, scoped_session
from Database import User, Media, Follower, Project, Connection, NecessitiesRequest
tableName = 'bos-db'
userName = 'root'
password = ''

conn = sqla.create_engine('mysql+pymysql://' + userName + ':' + password + '@localhost/' + tableName + '?charset=utf8')
Session = scoped_session(sessionmaker(bind=conn))


class Persister:

	def __init__(self):
		print("creating perister")

	def storeObject(self, object):
		db = Session()
		try:
			db.add(object)
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True

	def deleteObject(self, object):
		db = Session()
		print(object)
		try:
			db.delete(object)
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True
	
	#gets a user object by id, returns user object or False
	def getUserById(self, id):
		db = Session()
		user = db.query(User).filter(User.id == id).first()
		db.close()
		if user is not None:
			return user
		return False

	def checkUserExists(self, id):
		db = Session()
		user = db.query(User).filter(User.id == id).first()
		db.close()
		if user is not None:
			return True
		return False

	#gets a user object by email, returns user object or False
	def getUserByEmail(self, email):
		db = Session()
		user = db.query(User).filter(User.email == email.lower()).first()
		db.close()
		if user is not None:
			return user
		return False

	#sets a user's authenticated field in db on True to indicate that the user is logged in
	def setAuthenticated(self, email):
		db = Session()
		try:
			user = db.query(User).filter(User.email == email.lower()).first()
			user.authenticated = True
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True

	def setNotAuthenticated(self, email):
		db = Session()
		try:
			user = db.query(User).filter(User.email == email.lower()).first()
			user.authenticated = False
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True

	def getMediaById(self,id):
		db = Session()
		media = db.query(Media).filter(Media.id == id).first()
		db.close()
		if media is not None:
			return media
		return False

	def getFollowerById(self,id):
		db = Session()
		follower = db.query(Follower).filter(Follower.id == id).first()
		db.close()
		if follower is not None:
			return follower
		return False

	def getProjectById(self,id):
		db = Session()
		project = db.query(Project).filter(Project.id == id).first()
		db.close()
		if project is not None:
			return project
		return False

	def checkFollowerExists(self, user, project):
		db = Session()
		follower = db.query(Follower).filter(Follower.user == user).filter(Follower.project == project).first()
		db.close()
		if follower is not None:
			return True
		return False

	def getFollowerByContext(self, user, project):
		db = Session()
		follower = db.query(Follower).filter(Follower.user == user).filter(Follower.project == project).first()
		db.close()
		if follower is not None:
			return follower
		return False

	def getFollowersByProject(self, project):
		db = Session()
		followers = db.query(Follower).filter(Follower.project == project).all()
		db.close()
		if followers is not None:
			return followers
		return False

	def checkProjectExists(self, id):
		db = Session()
		project = db.query(Project).filter(Project.id == id).first()
		db.close()
		if project is not None:
			return True
		return False

	def getAllEvents(self):
		db = Session()
		events = db.query(Event).all()
		db.close()
		return events

	def getChatId(self,owner, user):
		db = Session()
		if(db.query(Connection.id).filter(owner == Connection.owner).filter(user == Connection.user).count()):
			chatId = db.query(Connection.id).filter(owner == Connection.owner).filter(user == Connection.user).first()
			db.commit()
			db.close()
			return chatId
		else:
			return False

	def addLike(self, id):
		db = Session()
		try:
			like = db.query(Project.likes).filter(Project.id == id).first()
			like += 1
			db.commit()
			db.close()
			return True
		except:
			db.close()
			return False

	def removeLike(self, id):
		db = Session()
		like = db.query(Project.likes).filter(Project.id == id).first()
		if (like <= 0):
			db.close()
			return False
		else:
			like -= 1
			db.commit()
			db.close()
	
	def totalLikes(self, id):
		db = Session()
		like = db.query(Project.likes).filter(Project.id == id).first()
		db.commit()
		db.close()
		return like
	
	def getAllProjects(self):
		db = Session()
		if db.query(Project).count():
			projects = db.query(Project).order_by(Project.beginDate).all()
			db.close()
			return projects
		else:
			return {}

	def getAllRequests(self):
		db = Session()
		if db.query(Project).count():
			requests = db.query(NecessitiesRequest).order_by(NecessitiesRequest.createdAt).all()
			db.close()
			return requests
		else:
			return {}

	def getRequestById(self, id):
		db = Session()
		request = db.query(NecessitiesRequest).filter(NecessitiesRequest.id == id).first()
		db.close()
		if request is not None:
			return request
		return False


