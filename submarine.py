from tkinter import *
import time
from tkinter import Canvas

HEIGHT = 500
WIDTH = 800

win = Tk()
win.title('Подводная   лодка')
draw = Canvas(win, height=HEIGHT, width=WIDTH, bg='darkblue')
draw.pack()

ship_id = draw.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = draw.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 15
MID_X = WIDTH / 2
MID_y = HEIGHT / 2

draw.move(ship_id, MID_X, MID_y)
draw.move(ship_id2, MID_X, MID_y)
SHIP_spd = 10


def move_ship(event):
    if event.keysym == 'Up':
        draw.move(ship_id, 0, -SHIP_spd)
        draw.move(ship_id2, 0, -SHIP_spd)
    elif event.keysym == 'Down':
        draw.move(ship_id, 0, SHIP_spd)
        draw.move(ship_id2, 0, SHIP_spd)
    elif event.keysym == 'Left':
        draw.move(ship_id, -SHIP_spd, 0)
        draw.move(ship_id2, -SHIP_spd, 0)
    elif event.keysym == 'Right':
        draw.move(ship_id, SHIP_spd, 0)
        draw.move(ship_id2, SHIP_spd, 0)


draw.bind_all('<Key>', move_ship)

win.mainloop()

time.sleep(0.5)
