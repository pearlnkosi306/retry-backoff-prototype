import requests

response = requests.get("http://localhost:5002/stock")
print(response.status_code, response.json())
