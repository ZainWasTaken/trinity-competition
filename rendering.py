import env_sim
import main
from tkinter import *
s = env_sim.Simulation()
root = Tk()
res, width, height = s.get_frame()
print(res)
print(width)
print(height)
def click(evt):
	print ("clicked at x " + str(evt.x) + " y " + str(evt.y))
	print(main.speciesColorDictionary["Lion"])
	animal = canvas.create_rectangle(evt.x, evt.y, evt.x+50, evt.y+50, fill=main.speciesColorDictionary[renderAnimal])
canvas = Canvas(root, width=width, height=height)
def beginClickDetection(animal):
	global renderAnimal
	renderAnimal = animal
	canvas.bind("<Button-1>", click)
def endClickDetection():
	canvas.unbind("<Button-1>")
canvas.pack()
beginClickDetection("Lion")
root.mainloop()

