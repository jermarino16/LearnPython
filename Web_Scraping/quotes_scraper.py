from bs4 import BeautifulSoup
import csv
import requests
from random import choice

response = ""
soup = ""
quotes = ""
default_url = "http://quotes.toscrape.com"
current_url = ""
list_of_quotes = []
hint_count = 0

#get url and quotes info
def get_info_from_url(url=default_url):
	global response
	global soup 
	global quotes

	# print("Getting info for " + url)

	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	quotes = soup.find_all("div", class_="quote")
	# print(quotes)
	# print("Scraping " + url)

def scrape_single_page():
	global list_of_quotes
	quote_information = []
	#scrape quotes on a page
	for quote in quotes:
		quote_information.clear()
		# print(quotes)
		quote_text = quote.find("span", class_="text").get_text()
		# print(quote_text)
		author = quote.find("small", class_="author").get_text()
		# print(author)
		url = quote.find("a")["href"]
		# print(url)

		#add info to a list
		quote_information.append(quote_text)
		quote_information.append(author)
		quote_information.append(url)
		# print(quote_information)

		#add this quote to a list of the quotes
		list_of_quotes.append(list.copy(quote_information))
		


def first_scrape():
	get_info_from_url()
	scrape_single_page()

def scrape_more_pages(url=default_url):
	# print("Getting info for " + url)
	get_info_from_url(url)
	scrape_single_page()

def keep_scraping():
	next_tag = soup.find("li", class_="next") # get the tag of next page to scrape
	# print(next_tag)
	#keep scraping until done
	while next_tag:
		next_href = next_tag.find("a")["href"]
		# print (next_href)
		current_url = default_url + next_href
		# print("current url is " + current_url)
		scrape_more_pages(current_url)
		next_tag = soup.find("li", class_="next")

def get_random_quote():
	return choice(list_of_quotes)

def get_author_birth_info(author_bio_url):
	get_info_from_url(default_url + author_bio_url)
	# print(default_url + author_bio_url)
	author_birth_date = soup.find("span", class_="author-born-date").get_text()
	author_birth_location = soup.find("span", class_="author-born-location").get_text()
	print("The author was born on " + author_birth_date)
	print("The author was born " + author_birth_location)

def give_hint(quote_information):
	global hint_count
	author_full_name = quote_information[1].split()
	author_href = quote_information[2]
	num_of_names = len(author_full_name)

	if hint_count == 0:
		get_author_birth_info(author_href)
		hint_count += 1

	elif hint_count == 1:
		print("The author's first name starts with a " + author_full_name[0][0])
		hint_count += 1

	elif hint_count == 2:
		print("The author's last name starts with a " + author_full_name[num_of_names -1 ][0])
		hint_count += 1

	elif hint_count == 3:
		if num_of_names == 3:
			print("The author has a middle name")
		else:
			print("The author does not have a middle name")
			hint_count += 1
	else:
		print("Sorry no more hints")

def write_rows_to_csv():
	with open ("quotes.csv", "w", newline="") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerows(list_of_quotes)

def play_game():
	#now time to loop through a game
	user_wants_to_play = True
	user_is_wrong = True
	global hint_count
	while user_wants_to_play:
		hint_count = 0 
		random_quote = get_random_quote()
		random_quote_text = random_quote[0]
		random_quote_author = random_quote[1]
		random_quote_url = random_quote[2]

		# print(random_quote_author)

		print("Alright Here's a quote")
		print(random_quote_text)

		#user gets 5 tries to guess it
		for x in range(0,5):
			user_guess = input("\nWho said it? ")
			if user_guess == random_quote_author:
				print("\nWow Good Job!")
				break
			else:
				give_hint(random_quote)

		print("\nThe author's name is " + random_quote_author)

		play_again = input("Do you want to play again? Type n for no: ")
		if play_again == "n":
			user_wants_to_play = False
		else:
			print("Okay let's go again!\n")	
#scrape at least once
first_scrape()
keep_scraping()
write_rows_to_csv()
# print(list_of_quotes)
play_game()
print("Awesome thanks for playing!")


	


