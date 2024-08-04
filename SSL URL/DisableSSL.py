import requests

response = requests.get('https://www.example.com', verify=False)
print(response.text)
