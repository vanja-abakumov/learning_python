from random import randint

from submarine_project.global_def import HEIGHT, WIDTH, MID_X, MID_y, MIN_BUB_R, MAX_BUB_R, MAX_BUB_SPD, SHIP_STEP, GAP
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
