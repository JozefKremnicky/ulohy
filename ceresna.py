import tkinter
canvas = tkinter .Canvas()
canvas.pack()
canvas.create_rectangle(70,80,90,180,fill='black')
canvas.create_oval(20,30,140,120,fill='green',outline='')
canvas.create_line(100,60,90,75,width=3)
canvas.create_line(100,60,110,75,width=3)
canvas.create_oval(85,70,95,80,fill='red')
canvas.create_oval(105,70,115,80,fill='red')

