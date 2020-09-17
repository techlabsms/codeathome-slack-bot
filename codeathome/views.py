from django.shortcuts import render
from django.http import HttpResponse
import os
from slack import WebClient
from slack.errors import SlackApiError

def home(request):
    global token
    token = os.environ['SLACKBOTTOKEN']
    client = WebClient(token=token)
    response = client.chat_postMessage(
        channel='#random',
        text="Hello world!")
    assert response["message"]["text"] == "Hello world!"
    return HttpResponse(f'<p>Token {token}</p>')


def testbot(request):
    global token
    token = os.environ['SLACKBOTTOKEN']
    client = WebClient(token=token)
    response = client.chat_postMessage(
        channel='C019CD1JL7Q',
        text="Testbot Recieved!")
    
    return HttpResponse(f'Its 80 degrees right now.', status=200)