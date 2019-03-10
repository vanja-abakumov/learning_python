from tkinter import *
import time


# Рисует координатные оси
def draw_axis(canvas):
    # рисуем оси координат
    canvas.create_line(10, 10, 500, 10, width=3, arrow=LAST)
    canvas.create_line(10, 10, 10, 500, width=3, arrow=LAST)

    for i in range(0, size, 50):
        canvas.create_text(i, 30, text=str(i), fill="purple", font=("Helvectica", "10"))
        canvas.create_text(30, i, text=str(i), fill="purple", font=("Helvectica", "10"))
        canvas.create_line(10, 10, 10, 500, width=3, arrow=LAST)


def blink(canvas, fig1, fig2):
    canvas.itemconfig(fig1, fill='green')
    canvas.itemconfig(fig2, state=HIDDEN)


def unblink(canvas, fig1, fig2):
    canvas.itemconfig(fig1, fill='white')
    canvas.itemconfig(fig2, state=NORMAL)


size = 500

win = Tk()
win.title('чужойц')
draw = Canvas(win, height=size, width=size)
draw.pack()
draw_axis(draw)  # Рисуем оси

body = draw.create_oval(100, 150, 300, 250, fill="green")
eye = draw.create_oval(170, 70, 230, 130, fill="white")
eyeball = draw.create_oval(190, 90, 210, 110, fill="black")
mouth = draw.create_oval(150, 220, 250, 240, fill="red")
neck = draw.create_line(200, 150, 200, 130, width=10)
hat = draw.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')
words = draw.create_text(200, 280, text='я  идиот')

while True:
    blink(draw, eye, eyeball)
    win.update()
    time.sleep(0.5)

    unblink(draw, eye, eyeball)
    win.update()
    time.sleep(0.5)
