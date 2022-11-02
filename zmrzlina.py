import tkinter
canvas = tkinter.Canvas(width=300,height=400,background='white')
canvas.pack()
canvas.create_oval(60,50,118,95,fill='red')
canvas.create_oval(40,70,110,140,fill='yellow')
canvas.create_oval(75,70,140,140,fill='green')
canvas.create_line(40,140,140,140,85,300,40,140)
canvas.create_rectangle(40,110,140,140,fill='white')
