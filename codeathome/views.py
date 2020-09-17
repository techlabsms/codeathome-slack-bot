from django.shortcuts import render
from django.http import HttpResponse
import os
def home(request):
    token= os.environ['SLACKBOTTOKEN']
    return HttpResponse(f'<p>Token {token}</p>')
