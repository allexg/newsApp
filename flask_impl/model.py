import json

class News(dict):
    def __init__(self, title, summary, publishedDate, link, imageURL = None, content = None):
        self.title = title
        self.summary = summary
        self.content = content
        self.publishedDate = publishedDate
        self.link = link
        self.imageURL = imageURL
        dict.__init__(self, title = title, summary = summary,
                      publishedDate = publishedDate, content = content, link = link, imageURL = imageURL)

