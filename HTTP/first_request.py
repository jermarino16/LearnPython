import requests
url = "http://google.com"

response = requests.get(url)

print(f"Your request to {url} is status code: {response.status_code}")