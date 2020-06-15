import json
from urllib.request import urlopen

'''
Simple Email Checker
'''

email = input("Email : ")

key = "YdJMzmBP6hkHxQsWcjwbZT8nLf7rVFUq" #ApiKey

url = "https://emailverifierapi.com/v2/?apiKey=" + key + "&email=" + email

response = urlopen(url)
data = json.load(response)
details=data['details']

if details == "The mailbox exists.":
    print("True Email!")
else:
    print("Fake Email!")
