import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nhk.or.jp/")
soup = BeautifulSoup(r.content,"html.parser")
#sel = soup.select("div.title a")
ul = soup.find_all('ul',class_="prime-news__list")
#b = ul.find_all("a")
print(ul)
#print(b)

