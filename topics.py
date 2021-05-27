import requests
import csv
from bs4 import BeautifulSoup as bs
from lxml import etree
import json



def TopicURLs(Enter):
    links = []
    page = requests.get(Enter)
    soup = bs(page.content, 'html.parser')
    tree = soup.find_all('a',attrs={"aria-label":True})
    for node in tree:
        tl = str(node).index('href="')+len('href="')
        ts1=str(node)[tl:]
        ts2= ts1[:ts1.index('"')]
        if(node.find('https://medium.com/topic/') != -1):
            links.append([ts2])
    url = [item[0] for item in links]
    return(url)

medium = 'https://medium.com/topics'

topics = TopicURLs(medium)

with open('Articles.json', 'w') as put:
    json.dump(topics, put)


# hotTable - article URL - selenium clapping and commenting
