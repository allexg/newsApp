from newsapi import NewsApiClient
import pprint

apiKey1 = 'ee943d29e158445a94e6287b6d65ab2a'
apiKey2 = '6735c00583ed4884a7f21bbbdae236ef'


newsapi = NewsApiClient(api_key=apiKey1)


top_headlines = newsapi.get_top_headlines(country='us', page_size=100)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(top_headlines['articles'])

# # /v2/everything
# all_articles = newsapi.get_everything(q='paris')
# print(all_articles)
#
# # /v2/sources
# sources = newsapi.get_sources()
# print(sources)# /v2/everything
# all_articles = newsapi.get_everything(q='paris')
# print(all_articles)
#
# # /v2/sources
# sources = newsapi.get_sources()
# print(sources)
