import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import extract

tableName = 'bos-db'
userName = 'root'
password = ''

conn = sqla.create_engine('mysql+pymysql://' + userName + ':' + password + '@localhost/' + tableName + '?charset=utf8')

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sqla.Column('name', sqla.VARCHAR(64))
    email = sqla.Column('email', sqla.VARCHAR(64), unique=True)
    password = sqla.Column('password', sqla.VARCHAR(64))
    authenticated = sqla.Column('authenticated', sqla.Boolean)


Base.metadata.create_all(conn)