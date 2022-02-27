import env_sim
from tkinter import *
s = env_sim.Simulation()
root = Tk()
def click(evt):
	print ("clicked at x " + str(evt.x) + " y " + str(evt.y))
canvas = Canvas(root, width=1280, height=720)
canvas.bind("<Button-1>", click)
canvas.pack()
root.mainloop()
