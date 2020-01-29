import requests
import json
from groupme_files.token_manager import TOKEN

def send_groupme_message(message):
    args = {"bot_id" : TOKEN, "text" : message}
    response = requests.post('https://api.groupme.com/v3/bots/post', data = args)
    return response