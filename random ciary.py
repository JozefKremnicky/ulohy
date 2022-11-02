import tkinter
from random import*
canvas = tkinter.Canvas()
canvas.pack()

def ciary():
    x = randint(80,400)
    y = randint(80,400)
    canvas.create_line(x,y,y,x,y)
for i in range(1,30):
    ciary()

                      
