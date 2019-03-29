import feedparser
from newsapi import NewsApiClient
import pprint

import json
import model


apiKey1 = 'ee943d29e158445a94e6287b6d65ab2a'
apiKey2 = '6735c00583ed4884a7f21bbbdae236ef'

newsapi = NewsApiClient(api_key=apiKey2)


def getTechnologyNews():
    news_list = []
    top_headlines = newsapi.get_top_headlines(category='technology', country='us', page_size=100)
    for headline in top_headlines['articles']:
        title = headline['title']
        summary = headline['description']
        content = headline['content']
        publishedDate = headline['publishedAt']
        link = headline['url']
        imageURL = headline.get('urlToImage')
        news = model.News(title, summary, publishedDate, link, imageURL, content)
        news_list.append(news)
    return json.dumps(news_list, indent=5)


def getBusinessNews():
    news_list = []
    top_headlines = newsapi.get_top_headlines(category='business', country='us', page_size=100)
    for headline in top_headlines['articles']:
        title = headline['title']
        summary = headline['description']
        content = headline['content']
        publishedDate = headline['publishedAt']
        link = headline['url']
        imageURL = headline.get('urlToImage')
        news = model.News(title, summary, publishedDate, link, imageURL, content)
        news_list.append(news)
    return json.dumps(news_list, indent=5)




# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(getPoliticsNews())
getTechnologyNews()