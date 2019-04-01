from flask import Flask
from flask import request
from flask import abort
import get_news as news
import asyncio
import websockets

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username


def get_news(inputCategory,inputLanguage,inputCountry):
    category = inputCategory
    language = inputLanguage
    country = inputCountry

    if category == 'technology' or category == "business" or category == "entertainment"\
            or category == "general" or category == "health" or category == "science" or category == "sports":
        return news.get_news(category,country,language)
    else:
        abort(404)


async def webSocketConnection(websocket, path):
	print("Il astept pe Domnu' Ogar Stefane \n")
	info = await websocket.recv()  # info primita de la Ogar Stefanel speram noi intr-un format firesc => category/country/language

	category = "technology"
	country = "us"
	language = "it"
	print(f"< {info}")

	actualNews = get_news(category,language,country)
	await websocket.send(actualNews)
# deal with webSocketS Connection Server-Side


# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code> or  <code>/news</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'
# application = Flask(__name__)
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))
# application.add_url_rule('/news', 'news', view_func=get_news)
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))



if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    #application.run()
	start_server = websockets.serve(webSocketConnection, 'localhost', 8000)
	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()
