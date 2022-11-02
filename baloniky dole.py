import tkinter, random
canvas= tkinter.Canvas(width=600,height=600)
canvas.pack()
for i in range(1,9):
    canvas.create_line(i*35,440,150,220)

def balony(x,y):
    farba = random.choice(('darkgreen','chartreuse','blueviolet','dodgerblue','orange','darkkhaki'))
    canvas.create_oval(x+5,y+5,x+50,y+50,fill=farba)



for i in range(1,9):
    balony(i*30,410)
