import requests

url = 'http://127.0.0.1:8000/callback'
atom_feed = open('atom_feed.xml', 'rb')  # Ensure the path is correct

response = requests.post(url, data=atom_feed)
print(response.text)
