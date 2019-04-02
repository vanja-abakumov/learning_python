from random import randint


def create_bubble(HEIGHT, WIDTH, MIN_BUB_R, MAX_BUB_R, MAX_BUB_SPD, draw, bub_id, bub_r, bub_speed):
    GAP = 100
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = draw.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


def move_ship(event, SHIP_STEP, draw, ship_id, ship_id2):
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


def move_bubbles(draw, bub_id, bub_speed):
    for i in range(len(bub_id)):
        draw.move(bub_id[i], -bub_speed[0], 0)

