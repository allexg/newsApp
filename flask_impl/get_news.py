from newsapi import NewsApiClient
import aws_translate as translate

import json
import model

apiKey1 = 'ee943d29e158445a************'

newsapi = NewsApiClient(api_key=apiKey1)

def get_news(category, country, language):
    news_list = []
    top_headlines = newsapi.get_top_headlines(category=category, country=country, page_size=100)
    for headline in top_headlines['articles']:
        title = headline['title']
        if title is not None:
            if title != '':
                title = translate.translate_text(title, language)
        summary = headline['description']
        if summary is not None:
            if summary != '':
                summary = translate.translate_text(summary, language)
        content = headline['content']
        if content is not None:
            if content != '':
                content = translate.translate_text(content, language)
        publishedDate = headline['publishedAt']
        link = headline['url']
        imageURL = headline.get('urlToImage')
        news = model.News(title, summary, publishedDate, link, imageURL, content)
        news_list.append(news)

    return json.dumps(news_list, indent=5)


