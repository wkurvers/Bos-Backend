import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import extract

dbName = 'bos-db'
userName = 'root'
password = ''

conn = sqla.create_engine('mysql+pymysql://' + userName + ':' + password + '@localhost/' + dbName + '?charset=utf8')

Base = declarative_base()

class User(Base):
	__tablename__ = 'User'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	name = sqla.Column('name', sqla.VARCHAR(64))
	email = sqla.Column('email', sqla.VARCHAR(64), unique=True)
	password = sqla.Column('password', sqla.VARCHAR(64))
	authenticated = sqla.Column('authenticated', sqla.Boolean)
	locationCity = sqla.Column('locationCity', sqla.VARCHAR(64))
	profilePhoto = sqla.Column('profilePhoto', sqla.VARCHAR(500))
	description = sqla.Column('description', sqla.VARCHAR(1000))
	organisation = sqla.Column('organisation', sqla.VARCHAR(64))

class Project(Base):
	__tablename__ = 'Project'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	title = sqla.Column('title', sqla.VARCHAR(64))
	description = sqla.Column('description', sqla.VARCHAR(1000))
	thumbnail = sqla.Column('thumbnail', sqla.VARCHAR(500))
	creator = sqla.Column('creator',sqla.Integer,sqla.ForeignKey('User.id'))
	beginDate = sqla.Column('beginDate',sqla.DATETIME)
	endDate = sqla.Column('endDate',sqla.DATETIME)
	createdAt = sqla.Column('createdAt',sqla.DATETIME)
	likes = sqla.Column('likes', sqla.Integer)

class Event(Base):
	__tablename__ = 'Event'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	title = sqla.Column('title', sqla.VARCHAR(64))
	description = sqla.Column('description', sqla.VARCHAR(1000))
	project = sqla.Column('project',sqla.Integer,sqla.ForeignKey('Project.id'))
	beginDate = sqla.Column('beginDate',sqla.DATETIME)
	endDate = sqla.Column('endDate',sqla.DATETIME)
	createdAt = sqla.Column('createdAt',sqla.DATETIME)

class Media(Base):
	__tablename__ = 'Media'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	project = sqla.Column('project',sqla.Integer,sqla.ForeignKey('Project.id'))
	name = sqla.Column('name', sqla.VARCHAR(64))
	mediaPath = sqla.Column('mediaPath', sqla.VARCHAR(500))

class Follower(Base):
	__tablename__ = 'Follower'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	project = sqla.Column('project',sqla.Integer,sqla.ForeignKey('Project.id'))
	user = sqla.Column('user', sqla.Integer, sqla.ForeignKey('User.id'))

class Connection(Base):
	__tablename__ = 'Connection'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	owner = sqla.Column('owner',sqla.Integer,sqla.ForeignKey('User.id'))
	user = sqla.Column('user', sqla.Integer, sqla.ForeignKey('User.id'))

class ConnectionRequest(Base):
	__tablename__ = 'ConnectionRequest'
	id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
	owner = sqla.Column('owner',sqla.Integer,sqla.ForeignKey('User.id'))
	user = sqla.Column('user', sqla.Integer, sqla.ForeignKey('User.id'))
	project = sqla.Column('project',sqla.Integer,sqla.ForeignKey('Project.id'))
	accepted = sqla.Column('accepted', sqla.Boolean)

Base.metadata.create_all(conn)