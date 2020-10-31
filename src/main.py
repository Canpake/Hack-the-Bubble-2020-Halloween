import wordlist
import paint
from tkinter import *

class Menu(object):

    def __init__(self):
        self.root = Tk()

        self.draw_button = Button(self.root, text='Start Game', command=self.open_paint)
        self.draw_button.grid(row=0, column=0)

        self.root.mainloop()

    def open_paint(self):
        self.root.destroy()
        paint.Paint()




if __name__ == '__main__':
    Menu()