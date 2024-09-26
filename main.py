from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.find("a").get("href"))
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_upvoted = article_upvotes.index(max(article_upvotes))
print(article_texts[most_upvoted])
print(article_links[most_upvoted])
