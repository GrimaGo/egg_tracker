from time import sleep
from sys import argv

from pprint import pprint
from telepot.loop import MessageLoop
import telepot

from telepot.delegate import per_inline_from_id, create_open, pave_event_space

from db_helper import DB


class InlineHandler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    def __init__(self, *args, **kwargs):
        super(InlineHandler, self).__init__(*args, **kwargs)

    def on_inline_query(self, msg):
        def compute_answer():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)

            #TODO: Hay que usar el query_string para proponer las alternativas
            articles = [{'type': 'photo',
                             'id': 'bulbasaur', 
                             'photo_url': 'http://vignette2.wikia.nocookie.net/world-fighters/images/5/5a/Bulbasaur6.jpg/revision/latest?cb=20160207231921',
                             'thumb_url': 'http://vignette2.wikia.nocookie.net/world-fighters/images/5/5a/Bulbasaur6.jpg/revision/latest?cb=20160207231921'},
						{'type': 'photo',
                             'id': 'charmander', 
                             'photo_url': 'https://s-media-cache-ak0.pinimg.com/736x/79/d9/7c/79d97cd68801eb29a4a5a33e208fb2ff--pokemon-charmander-google-search.jpg',
                             'thumb_url': 'https://s-media-cache-ak0.pinimg.com/736x/79/d9/7c/79d97cd68801eb29a4a5a33e208fb2ff--pokemon-charmander-google-search.jpg'},
						{'type': 'photo',
                             'id': 'squirtle', 
                             'photo_url': 'https://vignette4.wikia.nocookie.net/flutterbutter/images/f/f3/Squirtle.jpg/revision/latest?cb=20140913152539',
                             'thumb_url': 'https://vignette4.wikia.nocookie.net/flutterbutter/images/f/f3/Squirtle.jpg/revision/latest?cb=20140913152539'},
                        ]

            return articles
 	
        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        from pprint import pprint
        pprint(msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')

        #TODO: Hay que usar el result_id para guardar el hatch en la base de datos
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)


TOKEN = argv[1]

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_inline_from_id(), create_open, InlineHandler, timeout=10),
])

MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    sleep(10)