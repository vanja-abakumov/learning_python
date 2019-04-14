from random import randint
from math import sqrt

from submarine_project.global_def import HEIGHT, WIDTH, MIN_BUB_R, MAX_BUB_R, MAX_BUB_SPD, SHIP_STEP, GAP, SHIP_R
from submarine_project.global_def import bub_id, bub_r, bub_speed


# отрисовывает пузырь на экране и записывает его характеристики ( имя, скорость и размер ) в три списка
def create_bubble(draw):
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = draw.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


# Осуществляет реакцию на нажытые стрелочки
def move_ship(event, draw, ship_id, ship_id2):
    if event.keysym == 'Up':
        draw.move(ship_id, 0, -SHIP_STEP)
        draw.move(ship_id2, 0, -SHIP_STEP)
    elif event.keysym == 'Down':
        draw.move(ship_id, 0, SHIP_STEP)
        draw.move(ship_id2, 0, SHIP_STEP)
    elif event.keysym == 'Left':
        draw.move(ship_id, -SHIP_STEP, 0)
        draw.move(ship_id2, -SHIP_STEP, 0)
    elif event.keysym == 'Right':
        draw.move(ship_id, SHIP_STEP, 0)
        draw.move(ship_id2, SHIP_STEP, 0)


# Обходит весь список имен существующих пузырей и двигает по экрану каждый из них
def move_bubbles(draw):
    for i in range(len(bub_id)):
        draw.move(bub_id[i], -bub_speed[i], 0)


# По имени пузыря вычисляет и возвращает координаты пузыря
def get_coords(id_num, draw):
    pos = draw.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


# Удаляет пузырь, по его имени
def del_bubble(i, draw):
    del bub_r[i]
    del bub_speed[i]
    draw.delete(bub_id[i])
    del bub_id[i]


# Удаляет пузыри уплывшие за экран
def clean_up_bubs(draw):
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = get_coords(bub_id[i], draw)
        if x < -GAP:
            del_bubble(i, draw)


# Вычисляет растояние между двумя пузырями
def distance(id1, id2, draw):
    x1, y1 = get_coords(id1, draw)
    x2, y2 = get_coords(id2, draw)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Возвращает количество очков
def collision(ship_id2, draw):
    points = 0
    for bub in range(len(bub_id) - 1, -1, -1):  # Обходит весь список пузырей сконца
        if distance(ship_id2, bub_id[bub], draw) < (SHIP_R + bub_r[bub]):  # Если лодка касается пузыря
            points += (bub_r[bub] + bub_speed[bub])  # Очки добавляются за кажэдый проткнутый пузырь
            del_bubble(bub, draw)  # Удаляем проткнутый пузырь
    return points



