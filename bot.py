from time import sleep
from sys import argv

from pprint import pprint
from telepot.loop import MessageLoop
import telepot

from db_helper import DB

bot = telepot.Bot(argv[1])

def handle(msg):
	db = DB("eggs.db")
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type)

	if content_type == "text":
		m = msg["text"]
		if m.startswith('/'):
			command, dist, pokemon = m.split()
			if command == "/hatch":
				db.add_egg(msg["from"], dist, pokemon)


MessageLoop(bot, handle).run_as_thread()

while 1:
	sleep(10)
