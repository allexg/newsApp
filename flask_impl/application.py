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



if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    #application.run()
	start_server = websockets.serve(webSocketConnection, 'localhost', 8000)
	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()
