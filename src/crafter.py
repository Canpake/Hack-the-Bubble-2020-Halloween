from tkinter import *

from src import main
from src import wordlist
import random


class Crafter(object):

    # Constants here
    DRAWING_HEIGHT = 50
    DRAWING_WIDTH = 50

    def __init__(self, drawing_dict):
        self.drawing_list = self.unionise_dict(drawing_dict)
        random.shuffle(self.drawing_list)
        self.root = Tk()
        self.players = len(drawing_dict.keys())
        self.drawings = len(self.drawing_list)

        # set up canvas
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, rowspan=self.drawings-1, columnspan=4)

        # crafting text
        self.craft_text = wordlist.get_term()

        self.images = []

        # buttons + labels
        self.craft_label = Label(self.root, text=self.craft_text)
        self.craft_label.grid(row=0, column=2)

        self.craft_button = Button(self.root, text='Craft!', command=self.craft)
        self.craft_button.grid(row=0, column=3)

        self.menu_button = Button(self.root, text='menu', command=self.open_menu)
        self.menu_button.grid(row=0, column=0)

        # generate button images on the side; also keep track of images
        self.image_buttons = []
        self.images = []
        for (i, drawing) in enumerate(self.drawing_list):
            from PIL import Image, ImageTk
            image = Image.open('../images/' + drawing + '.png')
            image = image.resize((Crafter.DRAWING_HEIGHT, Crafter.DRAWING_WIDTH), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
            image = ImageTk.PhotoImage(image)

            image_button = Button(self.root, text=drawing, command=lambda c=i: print(self.image_buttons[c].cget("text")))
            image_button.config(image=image, width=Crafter.DRAWING_HEIGHT, height=Crafter.DRAWING_WIDTH)
            image_button.grid(row=i, column=5)

            # add to list to stop garbage collection
            self.image_buttons.append(image_button)
            self.images.append(image)

        # create a couple of movable objects
        self.place_image(20, 20, "../images/bruh.png")
        self.place_image(50, 50, "../images/bruh_2.png")

        # bind drag-and-drop movement
        self._drag_data = {"x": 0, "y": 0, "item": None}    # this data is used to keep track of an item being dragged
        self.c.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.c.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.c.tag_bind("token", "<B1-Motion>", self.drag)

        self.root.mainloop()

    def place_image(self, x, y, image_path):
        """Create an image at the given coordinate"""
        img = PhotoImage(file=image_path)
        self.c.create_image(x, y, anchor=NW, image=img, tags="token")
        self.images.append(img)

    def add_drawing(self):
        print('test')


    def craft(self):
        pass

    def drag_start(self, event):
        """Beginning drag of an object"""
        # record the item and its location
        self._drag_data["item"] = self.c.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]

        # move the object the appropriate amount
        self.c.move(self._drag_data["item"], delta_x, delta_y)

        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def open_menu(self):
        self.root.destroy()
        main.Menu()

    def unionise_dict(self, dict):
        new_list = []
        for key in dict:
            new_list = new_list + dict[key]

        return new_list


if __name__ == '__main__':
    test_dict = {
        1: ['gross', 'robot', 'disorder'],
        2: ['munching', 'corn stalk', 'doom'],
        3: ['ominous', 'slime', 'piracy']
    }
    Crafter(test_dict)