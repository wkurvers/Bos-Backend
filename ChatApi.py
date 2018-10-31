import os

from flask import jsonify


def storeChatMessages(chatId,messageObject):

    path = "C:/Users/Wouter/IdeaProjects/BosBackend/chat"
    chatPath = path + chatId + ".txt"
    if(os.path.isfile(chatPath)):
        chatFile = open(chatPath, "a")
        chatFile.write(messageObject)
    else:
        chatFile = open(chatPath, "w+")
        chatFile.write(messageObject)

    chatFile.close()

def getChatMessages(chatId):

    path = "C:/Users/Wouter/IdeaProjects/BosBackend/chat"
    chatPath = path + chatId + ".txt"
    with open(path, 'r') as content_file:
        content = content_file.read()
        return jsonify({'messages': content})
