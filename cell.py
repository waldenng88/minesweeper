from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_count_label_obj = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_marked = False
        self.cell_button_obj = None
        self.x = x
        self.y = y

        # append objs to cell.all list
        Cell.all.append(self)

    def create_button_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_button_obj = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='grey',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            font=('Comic Sans MS', 16)
        )
        Cell.cell_count_count_label_obj = lbl

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.count_surrounding_mines == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            # if number of mines equal to cells, then winner winner chicken dinner
            if Cell.cell_count == settings.MINE_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Winner Winner Chicken Dinner", "Game Over", 0)
                sys.exit()

        # cancel click events after opened
        self.cell_button_obj.unbind('<Button-1>')
        self.cell_button_obj.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # return cell obj based on x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property  # read only
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),  # upper left
            self.get_cell_by_axis(self.x-1, self.y),    # left
            self.get_cell_by_axis(self.x-1, self.y+1),  # lower left
            self.get_cell_by_axis(self.x, self.y-1),    # above
            self.get_cell_by_axis(self.x+1, self.y-1),  # upper right
            self.get_cell_by_axis(self.x+1, self.y),    # right
            self.get_cell_by_axis(self.x+1, self.y+1),  # lower right
            self.get_cell_by_axis(self.x, self.y+1)     # under
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property  # read only
    def count_surrounding_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_open:  # can only open if closed
            Cell.cell_count -= 1
            self.cell_button_obj.configure(text=self.count_surrounding_mines)
            # replace text with new count
            if Cell.cell_count_count_label_obj:
                Cell.cell_count_count_label_obj.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
            self.cell_button_obj.configure(
                bg='SystemButtonFace'
            )
        self.is_open = True
        # open the cell

    def show_mine(self):
        # logic to blow up game
        self.cell_button_obj.configure(bg='red')

        ctypes.windll.user32.MessageBoxW(0, "Clicked on a Mine", "Game Over", 0)
        sys.exit()

    def right_click(self, event):
        if not self.is_marked:
            self.cell_button_obj.configure(
                bg='red'

            )
            self.is_marked = True
        else:
            self.cell_button_obj.configure(
                bg='SystemButtonFace'
            )
            self.is_marked = False

    @staticmethod
    def randomize_mines():
        mines = random.sample(
            Cell.all,
            settings.MINE_COUNT
        )
        for mine in mines:
            mine.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
