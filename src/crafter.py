from tkinter import *

from src import main
from src import wordlist


class Paint(object):

    # Constants here

    def __init__(self):
        self.setup()

        self.craft_label = Label(self.root, text=self.craft_text)
        self.craft_label.grid(row=0, column=2)

        self.craft_button = Button(self.root, text='Craft!', command=self.craft)
        self.craft_button.grid(row=2, column=2)

        self.menu_button = Button(self.root, text='menu', command=self.open_menu)
        self.menu_button.grid(row=0, column=0)

        # create a couple of movable objects
        self.create_token(100, 100, "grey")
        self.create_token(200, 100, "black")

        # bind drag-and-drop movement
        self.c.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.c.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.c.tag_bind("token", "<B1-Motion>", self.drag)

        self.root.mainloop()

    def setup(self):
        self.root = Tk()

        # set up canvas
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=6)

        # crafting text
        self.craft_text = wordlist.get_term()

        # this data is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

    def create_token(self, x, y, color, image=None):
        """Create a token at the given coordinate in the given color"""
        self.c.create_oval(
            x - 25,
            y - 25,
            x + 25,
            y + 25,
            outline=color,
            fill=image,
            tags=("token",),
        )

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


if __name__ == '__main__':
    Paint()