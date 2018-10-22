# Bos-Backend
this is the repository storing the backend code for Team Optimum for the Battle of the Schools (2018)

It consist of the following main 3 files (read the end for explanation of the other files):

***1. Database.py***
   
   This file contains the code nessesary to connect to the database and generate its tables. To add more tables simply define a new        class that takes Base as a parameter, then define all the colums the table must have. use User as example:
 ```python
 class User(Base):
    __tablename__ = 'User'
    id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sqla.Column('name', sqla.VARCHAR(64))
    email = sqla.Column('email', sqla.VARCHAR(64), unique=True)
    password = sqla.Column('password', sqla.VARCHAR(64))
    authenticated = sqla.Column('authenticated', sqla.Boolean)
```
***2. Persister.py***
   
   When the server is running the Persister is the class responsible for the direct communication the the database, its main task are:
   1. storing objects, f.e. a new user
   2. removing objects, f.e. a user that has terminated his/hers account
   3. getting objects, f.e. getting a user with a certain id
   
   If you want to add new methods make sure to first open a session,
   ```python
   db = Session()
   ```
   commiting when you made a change to data in the database,
   ```python
   db.commit()
   ```
   and closing the session onces you're done,
   ```python
   db.close()
   ```
   For example code examin the storeObject method:
   ```python
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
   ```
***3. Server.py***
   
   This is the file that you run when you want to start the server.
   It defines all the routes that the server has, the server takes and returns *ONLY* json data.
   If you want to add a new route make sure the route name starts with a / and define with type of request it can accept (POST, GET, etc...). Then define a method and handle the request within. Use the register route as an example:
   ```python
   @app.route('/register', methods=['POST'])
    def registerUser():
	    data = request.get_json()
	    if data != None:
		    return jsonify({"response": userApi.saveUser(data.get('name'), data.get('email'), data.get('password'))})
	    return jsonify({"response": False, "msg": "Please make sure to send json data"})
   ```
***The remaining files***
It is customary to write a new class (in a new file) for each table that exists in the database. The name convention is [tablename]Api. All the tasks with datamanagement for that table must be handled in the [tablename]Api class of the relevant table. 
f.e. the register, login and logout tasks are all handled withen UserApi.py. The [tablename]Api doest *NOT* interact with the database directly, it simply calls relevant methods from the Persister. For an example of an Api class see below:
```python
from Database import User
import hashlib
from Persister import Persister

persister = Persister()

class UserApi():
	def __init__(self):
		print("creating userapi")

	def getUserById(self, id):
		return persister.getUserById(id)
```
