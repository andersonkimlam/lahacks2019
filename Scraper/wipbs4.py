import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://finance.yahoo.com/news/10-best-stocks-invest-now-183522645.html'
#Opens up a connection and grabs the page
uClient = uReq(my_url)
#Off-loads content into a variable
page_html = uClient.read()
#Closes off the connection
uClient.close()
#actual html parser
page_soup = soup(page_html, "html.parser")
#grab each "product"
