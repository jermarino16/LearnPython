from bs4 import BeautifulSoup
from csv import writer
import requests

response = ""
soup = ""
quotes = ""

#get url and quotes info
def get_info_from_url(url="http://quotes.toscrape.com", href=""):
	global response
	global soup 
	global quotes

	response = requests.get(url + href)
	soup = BeautifulSoup(response.text, "html.parser")
	quotes = soup.find_all("div", class_="quote")
	# print(quotes)

def scrape_single_page():
	#scrape quotes on a page
	for quote in quotes:
		# print(quotes)
		quote_text = quote.find("span", class_="text").get_text()
		# print(quote_text)
		author = quote.find("small", class_="author").get_text()
		# print(author)
		url = quote.find("a")["href"]
		print(url)


def first_scrape():
	get_info_from_url()
	scrape_single_page()

#scrape at least once
first_scrape()

#keep scraping until done




# print(quotes)
# list_of_information = []

#keep scraping pages until you get to the last page
# next_page = soup.find_all("li", class_="next")


