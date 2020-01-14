import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

#write to csv
with open("blog_data.csv", "w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["title", "link", "date"])

	# print(articles)
	for article in articles:
		# print(article.find("a").get_text())
		a_tag = article.find("a")
		title = a_tag.get_text()
		# print(a_tag['href'])
		url = a_tag['href']
		small_tag = article.find("small")
		# print(small_tag)
		date = small_tag.get_text()

		# print(title, url, date)
		csv_writer.writerow([title,url,date])