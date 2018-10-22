import Persister
from UserApi import UserApi
import os
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
app.secret_key = os.urandom(24)

userApi = UserApi()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def route(path):
	return render_template('index.html')

@app.route('/test', methods=['GET'])
def testServer():
	return jsonify({"working": True})

#POST request to register a new user
#Fields: 
#	name: string
#	email: string (must not be already in db)
#   password: string (unhashed)
@app.route('/register', methods=['POST'])
def registerUser():
	data = request.get_json()
	if data != None:
		return jsonify({"response": userApi.saveUser(data.get('name'), data.get('email'), data.get('password'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

#POST request to remove an existing user
#Fields:
#	id: int (must exist in db)
@app.route('/removeUser', methods=['POST'])
def removeUser():
	data = request.get_json()
	if data != None:
		return jsonify({"response": userApi.removeUser(data.get('id'))})
	return response({"response": False, "msg": "Please make sure to send json data"})

#POST request to login a user
#Fields:
#	email: string (must exist in db)
#	password: string (unhashed)
@app.route('/login', methods=['POST'])
def loginUser():
	data = request.get_json()
	if data != None:
		return jsonify({"response": userApi.loginUser(data.get('email'), data.get('password'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

#POST request to login a user
#Fields:
#	email: string (must exist in db)
@app.route('/logout', methods=['POST'])
def logoutUser():
	data = request.get_json()
	if data != None:
		return jsonify({"response": userApi.logoutUser(data.get('email'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)