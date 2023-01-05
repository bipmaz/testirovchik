from random import choice
import os
import time
import pyglet
errors = ['...', 'Серьезно?', 'Гугл не работает?']
result_question = ['Плюс в карму', 'Мое почтение, держи за ответы', 'Заслужил']
j = 0
class Question:

    def __init__(self, question, var1, var2, var3):
        self.question = question
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def print_question(self):
        message = self.question + '\n' + self.var1 + '\n'+ self.var2 + '\n'+ self.var3
        for i in message:
            time.sleep(0.05)
            print('\033[0m{}'.format(i), end='')

class Answer:

    def __init__(self, keys, answer):

        self.keys = keys
        self.answer = answer

    def answer_of_test(self):

        if self.answer == self.keys:
            global j
            j += 1
            variant = choice(result_question) + ' ' + str(j) + '\n'
            for symbol in variant:
                time.sleep(0.05)
                print("\033[32m{}".format(symbol), end='')

        else:
            variant = choice(errors) + '\n'
            for symbol in variant:
                time.sleep(0.5)
                print("\033[31m{}".format(symbol), end='')


def result(list_answer):

    if j >= len(list_answer)*0.75:
         message = 'Молодец, держи бездну'
         for i in message:
             print("\033[34m{}".format(i), end='')
             time.sleep(0.05)
         os.startfile('bezdna.gif')

    else:
         replika = 'Знаешь что?'
         for i in replika:
             print("\033[31m{}".format(i), end='')
             time.sleep(0.5)
         mus = pyglet.media.load('bad_end.mp3')
         mus.play()
         pyglet.app.event_loop.sleep(2)