import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker, scoped_session
from Database import User, Media, Follower, Project, Connection

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

    # gets a user object by id, returns user object or False
    def getUserById(self, id):
        db = Session()
        user = db.query(User).filter(User.id == id).first()
        db.close()
        if user is not None:
            return user
        return False

    # gets a user object by email, returns user object or False
    def getUserByEmail(self, email):
        db = Session()
        user = db.query(User).filter(User.email == email.lower()).first()
        db.close()
        if user is not None:
            return user
        return False

    # sets a user's authenticated field in db on True to indicate that the user is logged in
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

    def getMediaById(self, id):
        db = Session()
        media = db.query(Media).filter(Media.id == id).first()
        db.close()
        if media is not None:
            return media
        return False

    def getFollowerById(self, id):
        db = Session()
        follower = db.query(Follower).filter(Follower.id == id).first()
        db.close()
        if follower is not None:
            return follower
        return False

    def getProjectById(self, id):
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
            return False
        return True

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


    def getChatId(owner, user):
        db = Session()
        chatId = db.query(Connection.id).filter(owner == Connection.owner).filter(user == Connection.user).first()
        return chatId
        db.commit()
        db.close()
