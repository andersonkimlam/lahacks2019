import urllib
from urllib import request
import scrapy
from bs4 import BeautifulSoup
import re


from lxml import html
import requests

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0' )]

url = ('https://finance.yahoo.com/news/10-best-stocks-invest-now-183522645.html')
#url = ('https://finance.yahoo.com/news/top-stocks-buy-11-different-160641640.html')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl, features = 'lxml')

title = soup.title.text

myStocks = ['AAPL', 'XOM', 'INTL', 'NATH', 'GOOG', 'FB', 'NFLX', 'NVDA', 'UPS', 'GE', 'GM', 'UTX']

sentences = []
for i in range(len(myStocks)):
    pattern = re.compile(myStocks[i])
    body = soup.find('p', text = pattern)
    if body:

        sentences += [str(re.sub('[□\’]', '', body.text))]
outfile = open('./results.txt', 'w')
outfile.write(str(sentences))

url_gainers = 'https://finance.yahoo.com/gainers?offset=0&count=10'
page_gainers = requests.get(url_gainers)
tree_gainers = html.fromstring(page_gainers.content)
gainers = tree_gainers.xpath('//span[@class="Trsdu(0.3s) Fw(600) C($dataGreen)"]/text()')
#print(gainers)
# outfile_gainers = open('./results_gainers.txt', 'w')
# outfile_gainers.write(str(gainers)[1:-1])

url_stocks_gainers = 'https://finance.yahoo.com/gainers?offset=0&count=10'
page_stocks_gainers = requests.get(url_stocks_gainers)
tree_stocks_gainers = html.fromstring(page_stocks_gainers.content)
stocks_gainers = tree_stocks_gainers.xpath('//a[@class="Fw(600)"]/text()')
# outfile_stocks_gainers = open('./results_stocks_gainers.txt', 'w')
# outfile_stocks_gainers.write(str(stocks_gainers)[1:-1])





url_losers = 'https://finance.yahoo.com/losers?offset=0&count=10'
page_losers = requests.get(url_losers)
tree_losers = html.fromstring(page_losers.content)
losers = tree_losers.xpath('//span[@class="Trsdu(0.3s) Fw(600) C($dataRed)"]/text()')
#print(losers)
# outfile_losers = open('./results_losers.txt', 'w')
# outfile_losers.write(str(losers)[1:-1])


url_stocks_losers = 'https://finance.yahoo.com/losers?offset=0&count=10'
page_stocks_losers = requests.get(url_stocks_losers)
tree_stocks_losers = html.fromstring(page_stocks_losers.content)
stocks_losers = tree_stocks_losers.xpath('//a[@class="Fw(600)"]/text()')
# outfile_stocks_losers = open('./results_stocks_losers.txt', 'w')
# outfile_stocks_losers.write(str(stocks_losers)[1:-1])


gainers_dict = {}
for x in range(len(stocks_gainers)):
    gainers_dict[stocks_gainers[x]] = gainers[x:x+2]


outfile_stocks_gainers = open('./results_stocks_gainers.txt', 'w')
outfile_stocks_gainers.write(str(gainers_dict))

losers_dict = {}
for x in range(len(stocks_losers)):
    losers_dict[stocks_losers[x]] = losers[x:x+2]


outfile_stocks_losers = open('./results_stocks_losers.txt', 'w')
outfile_stocks_losers.write(str(losers_dict))



#
# sentiment_scores = []
#
# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types
#
# # Instantiates a client
# client = language.LanguageServiceClient()
#
# for x in range(len(sentences)):
#     # The text to analyze
#     text = sentences[x]
#     document = types.Document(
#     content=text,
#     type=enums.Document.Type.PLAIN_TEXT)
#
# # Detects the sentiment of the text
#     sentiment = client.analyze_sentiment(document=document).document_sentiment
#     sentiment_scores += [sentiment.score]
#
#
#
# outfile_stocks_gainers = open('./results_sentiments.txt', 'w')
# outfile_stocks_gainers.write(str(sentiment_scores))
