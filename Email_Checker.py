import json
from urllib.request import urlopen

'''
Simple Email Checker
'''

email_checker = input("Email : ")

key = "BSnzI5Z8LFU7EVmyc9hARGTw2JvPKC0j"

url = "https://emailverifierapi.com/v2/?apiKey=" + key + "&email=" + email_checker
response = urlopen(url)
data = json.load(response)
details=data['details']

if details == "The mailbox exists.":
    print("True!")
else:
    print("False!")
