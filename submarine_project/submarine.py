from tkinter import *
from tkinter import Canvas
from random import randint
from time import sleep

from submarine_project.func import create_bubble, move_bubbles, move_ship, clean_up_bubs
from submarine_project.global_def import HEIGHT, WIDTH, MID_X, MID_y, MIN_BUB_R, MAX_BUB_R, MAX_BUB_SPD, SHIP_STEP

# Создали окно и холст в окне
win = Tk()
win.title('Подводная лодка')
draw = Canvas(win, height=HEIGHT, width=WIDTH, bg='darkblue')
draw.pack()

# Наррисовали подводную лодку
ship_id = draw.create_polygon(5, 5, 5, 25, 30, 15, fill='red')  # Треугольник
ship_id2 = draw.create_oval(0, 0, 30, 30, outline='red')        # Круг

# Поместили подводную лодку в средину холста
draw.move(ship_id, MID_X, MID_y)
draw.move(ship_id2, MID_X, MID_y)

# Свзали событие по нажатию стрелок с функцией, которая двигает подводную лодку
draw.bind_all('<Key>', lambda event: move_ship(event, draw, ship_id, ship_id2))

# Повторять бесконечно
while True:
    # Создаем только один пузырь из 10
    if randint(1, 10) == 1:
        create_bubble(draw)
    move_bubbles(draw)   # Передвигает все пузыри на экране
    clean_up_bubs(draw)  # Удаляет пузыри уплывшие за экран
    win.update()
    sleep(0.01)
