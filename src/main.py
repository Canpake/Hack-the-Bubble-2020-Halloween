from collections import defaultdict
from tkinter import *

from src import wordlist, crafter
from src import paint
from src import crafter
from src.wordlist import WordType

player_score = {
    1: 0,
    2: 0,
    3: 0
}


class Menu(object):

    def __init__(self):
        self.root = Tk()

        self.draw_button = Button(self.root, text='Start Game', command=self.start_game)
        self.draw_button.grid(row=0, column=0, columnspan=2)

        self.player_text = Label(self.root, text='Number of players:')
        self.player_text.grid(row=1, column=0)

        self.player_count = IntVar(self.root)
        self.player_count.set(3)

        self.player_select = OptionMenu(self.root, self.player_count, 3, 4, 5, 6, 7, 8)
        self.player_select.grid(row=1, column=1)

        self.root.mainloop()

    def start_game(self):
        count = self.player_count.get()
        player_drawings = []

        self.root.destroy()
        for i in range(1, count+1):
            player_score[i] = 0
            adjective, noun, descriptor = wordlist.get_new_word(WordType.ADJECTIVE), wordlist.get_new_word(WordType.NOUN), wordlist.get_new_word(WordType.DESCRIPTOR)
            player_drawings.extend([adjective, noun, descriptor])

            paint.Paint(i, wordlist.get_new_word(WordType.ADJECTIVE))
            paint.Paint(i, wordlist.get_new_word(WordType.NOUN))
            paint.Paint(i, wordlist.get_new_word(WordType.DESCRIPTOR))

        crafter.Crafter(player_drawings)




if __name__ == '__main__':
    Menu()