import tkinter
canvas=tkinter.Canvas()
canvas.pack()
canvas.create_oval(100,60,150,110,fill='blue')
canvas.create_line(100,80,125,170)
canvas.create_line(150,80,125,170)
canvas.create_rectangle(115,170,135,180,fill='red')
