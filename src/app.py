from helper.twilio_api import send_message
from helper.langchain_chat import create_conversation
from helper.templates import *
from flask import Flask, request
from dotenv import load_dotenv
import logging
load_dotenv()

app = Flask(__name__)
conversations_db = {}
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        message = request.form['Body']
        sender_id = request.form['From']
        response = executeAndSaveChat(sender_id, message)
        send_message(sender_id, response)
    except Exception as e:
        app.logger.exception("Exception occurred")
        print(f"error: {e}")
        pass
    return 'OK', 200

def executeAndSaveChat(sender_id, message):
    conversation = get_or_create_conversation(sender_id)
    response = conversation.predict(input=message)
    conversations_db[sender_id] = conversation
    return response

def get_or_create_conversation(sender_id):
    if not conversations_db.get(sender_id):
        conversation = create_conversation(template=first_contact_template)
    else:
        conversation = conversations_db.get(sender_id)
    return conversation

