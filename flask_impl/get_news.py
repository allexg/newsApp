import feedparser
from newsapi import NewsApiClient
import pprint

import json
import model


apiKey1 = '**************************'
apiKey2 = '************************'

newsapi = NewsApiClient(api_key=apiKey2)

def get_news(category, country):
    news_list = []
    top_headlines = newsapi.get_top_headlines(category=category, country=country, page_size=100)
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
#print(get_news("general", "us"))