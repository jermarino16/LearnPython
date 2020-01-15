from bs4 import BeautifulSoup
from csv import writer
import requests
from random import choice

response = ""
soup = ""
quotes = ""
default_url = "http://quotes.toscrape.com"
current_url = ""
list_of_quotes = []

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
		list_of_quotes.append(quote_information)
		


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

#scrape at least once
first_scrape()
keep_scraping()
# print(list_of_quotes)

print(choice(list_of_quotes))

## right now there are 10 quotes in one list. whhyyy



	


