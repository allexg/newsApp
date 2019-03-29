from flask import Flask
from flask import request
from flask import abort
import get_news as news
import json


def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username


def get_news():
    category = request.args.get('category')
    if category == 'technology':
        return news.getTechnologyNews()
    elif category == 'business':
        return news.getBusinessNews()
    else:
        abort(404)



header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code> or  <code>/news</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


application = Flask(__name__)


application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))


application.add_url_rule('/news', 'news', view_func=get_news)

application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))



if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()