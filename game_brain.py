import tkinter as tk
import random
from facts import Fact
from time import time, sleep


class MyApp(object):

    def __init__(self, tk_instance):
        self.tk_instance = tk_instance
        self.tk_instance.title = "Game"
        self.tk_instance.geometry('{}x{}'.format(850, 700))
        self.current_score = 0

        self.canvas = tk.Canvas(self.tk_instance, background="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.text_box = tk.Entry(self.tk_instance, width=6, font=("Arial", 18))
        self.text_box.pack()
        self.text_box.focus()
        self.button = tk.Button(self.tk_instance, height=1, width=10, text="Submit", command=self.check_input)
        tk_instance.bind('<Return>', self.check_input)
        # self.button.pack()

        self.score = tk.Label(self.tk_instance, font=("Arial", 18), text=f"score: {str(self.current_score)}", width=15)
        self.score.pack()

        self.facts = []
        self.start()

    # "the_event=None" is needed because when keyboard enter is hit it passes a param, but on button mouse click, nothing is passed
    def check_input(self, the_event=None):
        answer_try = int(self.text_box.get())
        print('input: ', answer_try)
        self.text_box.delete(0, 'end')
        for fact in self.facts:
            if fact.is_answer_value(answer_try):
                print('answer was correct!')
                self.current_score += 1
                self.facts.remove(fact)
                self.update_score()
        if self.current_score == 21:
            self.score['text'] = "YOU WIN!"
        elif self.current_score > 0 and self.current_score % 7 == 0:
            self.start()

    def update_score(self):
        print(f"current score: {self.current_score}")
        self.score['text'] = f"Score: {str(self.current_score)}"

    def start(self):
        for i in range(7):
            new_fact = Fact(self, 115 * i, random.randint(40, 80))
            self.facts.append(new_fact)
            new_fact.go()
