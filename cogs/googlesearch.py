import requests
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

query = 'how old is samuel l jackson'

## Google Search query results as a Python List of URLs
search_result_list = list(search(query, tld="google.com", num=10, stop=3, pause=1))

page = requests.get(search_result_list[index])

tree = html.fromstring(page.content)

soup = BeautifulSoup(page.content, features="lxml")