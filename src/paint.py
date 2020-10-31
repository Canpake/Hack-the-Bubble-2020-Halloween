from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.colorchooser import askcolor
import pyscreenshot
from src import main
from src import wordlist


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.save_button = Button(self.root, text='save', command=self.save)
        self.save_button.grid(row=0, column=0)

        self.menu_button = Button(self.root, text='menu', command=self.open_menu)
        self.menu_button.grid(row=0, column=3)

        self.draw_text = wordlist.get_descriptor()
        self.draw_label = Label(self.root, text='draw... ' + self.draw_text)
        self.draw_label.grid(row=0, column=1)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.set(self.DEFAULT_PEN_SIZE)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def save(self):
        from PIL import Image

        def get_window_rect():
            height = self.c.winfo_height()
            width = self.c.winfo_width()
            x1 = self.c.winfo_rootx()
            x2 = x1 + width
            y1 = self.c.winfo_rooty()
            y2 = y1 + height
            return (x1, y1, x2, y2)

        # file_name = asksaveasfilename(filetypes=[('PNG File (.png)', '.png')], defaultextension='.png')
        file_name = '../images/' + self.draw_text + '.png'

        if file_name:
            img = pyscreenshot.grab(bbox=get_window_rect())  # X1,Y1,X2,Y2
            img.save(file_name, "PNG")

            img = Image.open(file_name)
            img = img.convert("RGBA")
            datas = img.getdata()

            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)

            img.putdata(newData)
            img.save(file_name, "PNG")

            self.root.destroy()
            main.Menu()

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def open_menu(self):
        self.root.destroy()
        main.Menu()


if __name__ == '__main__':
    Paint()