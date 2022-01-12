import requests
from bs4 import BeautifulSoup

URL = input("Enter a full url: ")
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html5lib')
print(soup.prettify())

