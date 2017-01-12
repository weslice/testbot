from flask import Flask, request
import requests
import json
import traceback
import random
app = Flask(__name__)

token = "EAAa8E6VNt3EBADvH7cWPONPG8q10a2vkBDCDZAT8t3iml7TvGncZBZBljVZCZAH1tFGXI0DqXZB4CPAFE2NCm3qy1PCs3hB09OSfsRZCe0nv3Y9S9szKe0k9MTw6K6Owb6WQdA79gbJLk1nisUdCQHZCWnWxEb11TaETbr8T2ZB1DNgZDZD"
tas = requests.get('https://graph.facebook.com/v2.6/me?access_token=' + token)
      
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      payload = {'recipient': {'id': sender}, 'message': {'text': "Hello Wes" }} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == '<wes>':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)