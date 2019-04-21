from tkinter import *
from tkinter import Canvas
from random import randint
from time import sleep
import simpleaudio as sa

from submarine_project.func import create_bubble, move_bubbles, move_ship, clean_up_bubs, collision
from submarine_project.global_def import HEIGHT, WIDTH, MID_X, MID_y, SHIP_R, NUMBER_BUB, TIME_LIMIT, BONUS_SCORE

# Создали окно и холст в окне
win = Tk()
win.title('Подводная лодка')
draw = Canvas(win, height=HEIGHT, width=WIDTH, bg='darkblue')
draw.pack()

# Наррисовали подводную лодку
ship_id = draw.create_polygon(5, 5, 5, 25, 30, SHIP_R, fill='red')  # Треугольник
ship_id2 = draw.create_oval(0, 0, 30, 30, outline='red')  # Круг

# Поместили подводную лодку в средину холста
draw.move(ship_id, MID_X, MID_y)
draw.move(ship_id2, MID_X, MID_y)

# Свзали событие по нажатию стрелок с функцией, которая двигает подводную лодку
draw.bind_all('<Key>', lambda event: move_ship(event, draw, ship_id, ship_id2))

# Выводим надписи Time, Score и создаем поля для показа времени и очков
label_font = ("Purisa", 20)
value_font = ("Times", 20, "bold")
draw.create_text(50, 30, text='TIME', font=label_font, fill='white')
draw.create_text(150, 30, text='SCORE', font=label_font, fill='white')
time_text = draw.create_text(50, 150, font=value_font, fill='yellow')
score_text = draw.create_text(150, 63, font=value_font, fill='yellow')

# Проигрывает музыку в формате *.wav в фоне
wave_obj = sa.WaveObject.from_wave_file("boat.wav")
play_obj = wave_obj.play()

score = 0

# Повторять бесконечно
while True:
    # Создаем только один пузырь из NUMBER_BUB
    if randint(1, NUMBER_BUB) == 1:
        create_bubble(draw)
    move_bubbles(draw)  # Передвигает все пузыри на экране
    clean_up_bubs(draw)  # Удаляет пузыри уплывшие за экран
    score += collision(ship_id2, draw)
    draw.itemconfig(score_text, text=str(score))
    # draw.itemconfig(time_text, text=str(time_left))

    win.update()
    sleep(0.01)
