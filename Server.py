import ChatApi
import Persister
from UserApi import UserApi
from MediaApi import MediaApi
from FollowerApi import FollowerApi
import os
from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
app = Flask(__name__)
app.secret_key = os.urandom(24)

userApi = UserApi()
mediaApi = MediaApi()
followerApi = FollowerApi()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def route(path):
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def testServer():
    return jsonify({"working": True})


# POST request to register a new user
# Fields:
#	name: string
#	email: string (must not be already in db)
#   password: string (unhashed)
# 	locationCity: string
# 	profilePhoto: string (base64 image)
# 	description: string
# 	organisation: string
@app.route('/register', methods=['POST'])
def registerUser():
    data = request.get_json()
    if data != None:
        return jsonify({"response": userApi.saveUser(
            data.get('name'),
            data.get('email'),
            data.get('password'),
            data.get('locationCity'),
            data.get('profilePhoto'),
            data.get('description'),
            data.get('organisation')
        )})
    return jsonify({"response": False, "msg": "Please make sure to send json data"})


# POST request to remove an existing user
# Fields:
#	id: int (must exist in db)
@app.route('/removeUser', methods=['POST'])
def removeUser():
    data = request.get_json()
    if data != None:
        return jsonify({"response": userApi.removeUser(data.get('id'))})
    return jsonify({"response": False, "msg": "Please make sure to send json data"})


# POST request to login a user
# Fields:
#	email: string (must exist in db)
#	password: string (unhashed)
@app.route('/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    if data != None:
        return jsonify({"response": userApi.loginUser(data.get('email'), data.get('password'))})
    return jsonify({"response": False, "msg": "Please make sure to send json data"})


# POST request to login a user
# Fields:
#	email: string (must exist in db)
@app.route('/logout', methods=['POST'])
def logoutUser():
    data = request.get_json()
    if data != None:
        return jsonify({"response": userApi.logoutUser(data.get('email'))})
    return jsonify({"response": False, "msg": "Please make sure to send json data"})


@app.route('/storeChatMessages', methods=["POST"])
def storeChatMessages():
    messageObject = request.args.get('messageObject')
    chatId = request.args.get('chatId')
    ChatApi.storeChatMessages(chatId, messageObject)


@app.route('/getChatMessages', methods=["GET"])
def getChatMessages():
    return ChatApi.storeChatMessages()


@app.route('/storeMedia', methods=['POST'])
def storeMedia():
	data = request.get_json()
	if data != None:
		return jsonify({"response": mediaApi.storeMedia(data.get('project'), data.get('name'), data.get('media'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

@app.route('/removeMedia', methods=['POST'])
def removeMedia():
	data = request.get_json()
	if data != None:
		return jsonify({"response": mediaApi.removeMedia(data.get('id'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

@app.route('/addFollower', methods=['POST'])
def addFollower():
	data = request.get_json()
	if data != None:
		return jsonify({"response": followerApi.addFollower(data.get('project'), data.get('user'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

@app.route('/removeFollower', methods=['POST'])
def removeFollower():
	data = request.get_json()
	if data != None:
		return jsonify({"response": followerApi.removeFollower(data.get('id'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

@app.route('/getFollowersForProject', methods=['POST'])
def getFollowersForProject():
	data = request.get_json()
	if data != None:
		return jsonify({"response": followerApi.getFollowersForProject(data.get('project'))})
	return jsonify({"response": False, "msg": "Please make sure to send json data"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
