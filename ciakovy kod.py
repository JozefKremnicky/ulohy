import tkinter,random
canvas=tkinter.Canvas()
canvas.pack()
for i in range(1,20):
    sirka = random.randrange(2,7)
    canvas.create_line(i*10,10,i*10,200,width=sirka)

print( sirka)
