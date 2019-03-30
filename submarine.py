from tkinter import *
import time
HEIGHT=500
WIDTH = 800

win = Tk()
win.title('Подводная   лодка')
draw = Canvas(win, height=HEIGHT, width=WIDTH, bg='darkblue')
draw.pack()
win.mainloop()

time.sleep(0.5)
