from tkinter import *
from tkinter import Canvas
from random import randint
from time import sleep

from submarine_project.func import create_bubble, move_bubbles, move_ship

# ****** Секция инициализации переменных ******

HEIGHT = 500  # Высота холста
WIDTH = 800  # Ширина холста
MID_X = WIDTH / 2  # Средина холста по Х
MID_y = HEIGHT / 2  # Средина холста по Y
MIN_BUB_R = 10  # Минимальный размер ( радиус ) пузыря
MAX_BUB_R = 30  # Максимальный размер пузыря
MAX_BUB_SPD = 10  # Максимальная скрость пузыря
SHIP_STEP = 10  # Шаг перемещения подводной лодки
bub_id = list()  # Список имен пузырей
bub_r = list()  # Список размеров пузырей
bub_speed = list()  # Спсиок скоростей пузырей

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
draw.bind_all('<Key>', lambda event: move_ship(event, SHIP_STEP, draw, ship_id, ship_id2))

# Повторять бесконечно
while True:
    # Создаем только один пузырь из 10
    if randint(1, 10) == 1:
        create_bubble(HEIGHT, WIDTH, MIN_BUB_R, MAX_BUB_R, MAX_BUB_SPD, draw, bub_id, bub_r, bub_speed)
    move_bubbles(draw, bub_id, bub_speed)
    win.update()
    sleep(0.001)
