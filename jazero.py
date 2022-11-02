import tkinter, random
canvas=tkinter.Canvas(height=600,width=600,bg='white')
canvas.pack()

canvas.create_line(120,30,120,400,width=4)
canvas.create_rectangle(120,30,230,130,fill='green',width=3)
canvas.create_oval(30,280,200,400,fill='brown',outline='')
canvas.create_rectangle(0,300,600,600,outline='',fill='blue')
canvas.create_line(200,250,350,250,300,350,240,350,200,250,width=4)
canvas.create_line(270,250,270,40,290,150,270,180,width=4)
