import requests
import random

url = "https://icanhazdadjoke.com/search"

user_input = input("What type of dad jokes do you want? \n")

response = requests.get(
	url, 
	headers = {"Accept": "application/json"}, 
	params = { "term": user_input } )

data = response.json()

if(data["results"]):
	num_of_jokes = len(data["results"])
	random_number = random.randint(0, num_of_jokes - 1)

	print(f"There was {num_of_jokes} jokes: Here's one: \n {data['results'][random_number]['joke']}")
else:
	print(f"there are no jokes about {user_input}")