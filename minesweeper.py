from tkinter import *
import settings
import utility
from cell import Cell

root = Tk()

# settings of main window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg="grey")
root.title("minesweeper")
root.resizable(False, False)

# top frame
top_frame = Frame(
    root,
    bg="blue",
    width=utility.width_shifter(100),
    height=utility.height_shifter(20)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='blue',
    text='Minesweeper',
    font=('Comic Sans MS', 48)
)

game_title.place(
    x=utility.width_shifter(36), y=utility.height_shifter(7)
)

# center frame
center_frame = Frame(
    root,
    bg='green',
    width=utility.width_shifter(75),
    height=utility.height_shifter(75)
)
center_frame.place(
    x=utility.width_shifter(25),
    y=utility.height_shifter(25)
)

# left frame
left_frame = Frame(
    root,
    bg='grey',
    width=utility.width_shifter(25),
    height=utility.height_shifter(75)
)
left_frame.place(
    x=0,
    y=utility.height_shifter(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_obj(center_frame)
        c.cell_button_obj.grid(
            column=x,
            row=y
        )

# call label from Cell Class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_count_label_obj.place(x=utility.width_shifter(7), y=0)

Cell.randomize_mines()

# run
root.mainloop()
