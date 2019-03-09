from tkinter import *


# Рисует координатные оси
def draw_axis(canvas):
    # рисуем оси координат
    canvas.create_line(10, 10, 500, 10, width=3, arrow=LAST)
    canvas.create_line(10, 10, 10, 500, width=3, arrow=LAST)

    for i in range(0, size, 50):
        canvas.create_text(i, 30, text=str(i), fill="purple", font=("Helvectica", "10"))
        canvas.create_text(30, i, text=str(i), fill="purple", font=("Helvectica", "10"))
        canvas.create_line(10, 10, 10, 500, width=3, arrow=LAST)


size = 500

win = Tk()
draw = Canvas(win, height=size, width=size)
draw.pack()
draw_axis(draw)  # Рисуем оси
rect = draw.create_rectangle(100, 100, 300, 200, outline="red")
oval = draw.create_oval(100, 100, 300, 200, fill="blue")
win.mainloop()
