import sys
import urllib.request
import json

def addName():
    user = sys.argv[1]
    url = f'https://api.github.com/users/{user}/events'
    print(url)
    response = urllib.request.urlopen(url)
    print('Status code:', response.status)

addName()
