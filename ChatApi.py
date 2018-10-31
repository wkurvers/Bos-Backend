import os
import Persister
from flask import jsonify


def storeChatMessages(owner, user,messageObject):

    path = "C:/Users/Wouter/IdeaProjects/BosBackend/chat"
    chatId = Persister.getChatId(owner,user)
    chatPath = path + chatId + ".txt"
    if(os.path.isfile(chatPath)):
        chatFile = open(chatPath, "a")
        chatFile.write(messageObject)
    else:
        chatFile = open(chatPath, "w+")
        chatFile.write(messageObject)

    chatFile.close()

def getChatMessages(owner, user):

    path = "C:/Users/Wouter/IdeaProjects/BosBackend/chat"
    chatId = Persister.getChatId(owner,user)
    chatPath = path + chatId + ".txt"
    with open(chatPath, 'r') as content_file:
        content = content_file.read()
        return jsonify({'messages': content})
