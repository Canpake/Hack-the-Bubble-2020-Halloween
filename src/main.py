import wordlist
import paint
from tkinter import *

class Menu(object):

    def __init__(self):
        self.root = Tk()

        self.draw_button = Button(self.root, text='Start Game', command=self.open_paint)
        self.draw_button.grid(row=0, column=0)

        self.player_count = StringVar(self.root)
        self.player_count.set(3)

        self.player_select = OptionMenu(self.root, self.player_count, 3, 4, 5, 6, 7, 8)
        self.player_select.grid(row=0, column=1)

        self.root.mainloop()

    def open_paint(self):
        self.root.destroy()
        paint.Paint()

    def start_game(self):
        self.root.destroy()
        for i in range(0, self.player_count):
            pass





if __name__ == '__main__':
    Menu()