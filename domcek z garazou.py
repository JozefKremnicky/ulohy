import tkinter
canvas=tkinter.Canvas(width=600,height=400,bg='white')
canvas.pack()

def domcok():
    canvas.create_rectangle(10,90,110,220,fill='lime')
    canvas.create_line(10,90,60,20,110,90,fil='brown')
    canvas.create_rectangle(40,180,80,220,fill='black')
def garaz():
    canvas.create_rectangle(110,150,300,220,fill='burlywood')
def okna(x,y):
    canvas.create_rectangle(x+30,y+40,x+50,y+60,fill='blue')

canvas.create_oval(330,120,380,180,fill='green')
canvas.create_rectangle(350,180,360,220,fill='brown')

canvas.create_oval(400,120,450,180,fill='green')
canvas.create_rectangle(420,180,430,220,fill='brown')

domcok()
for i in range(0,2):        
    okna(i*40,70)

for i in range(0,2):        
    okna(i*40,110)
garaz()
canvas.create_rectangle(130,160,150,180,fill='blue')
    
canvas.create_rectangle(180,160,200,180,fill='blue')
canvas.create_rectangle(220,180,240,220,fill='black')

