import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import Canvas, ttk
from tkinter import colorchooser


root = tk.Tk()
root.geometry('800x800')
root.title('Slider Demo')





#animal values
class AnimalSettings:
	def __init__(self, name, x, y, left, right):	
		self.name = name
		self.x = x
		self.y = y
		
		hardiness_current_value = tk.DoubleVar()

		#animal labels
		animal_name_label = ttk.Label(
			root,
			text=self.name,
			font=font.Font(family = 'Lemon Milk',size=20) 
		)


		#Slider Label Locations
		animal_name_label.grid(
			column=self.x,
			row=self.y,
			sticky='w'
		)
		#animal labels
		hardiness_slider_label = ttk.Label(
			root,
			text=(left)
		)


		#Slider Label Locations
		hardiness_slider_label.grid(
			column=self.x-1,
			row=self.y+20,
			sticky='w'
		)
		#Animal Number Label
		hardiness_value_label = ttk.Label(
			root,
			text='{: .2f}'.format(hardiness_current_value.get())
		)
		#Find/Map Animal Sliders
		def hardiness_printval(event):
			hardiness_value_label.configure(text='{: .2f}'.format(hardiness_current_value.get()))
			scalenum=round(hardiness_current_value.get())
			print(scalenum)
		#Animal Sliders
		hardiness_slider = ttk.Scale(
			root,
			from_=0,
			to=100,
			orient='horizontal',  # vertical
			variable=hardiness_current_value,
			command=hardiness_printval
		)
		#Location for number and Slider
		#hardiness
		hardiness_value_label.grid(
			row=self.y+23,
			columnspan=self.x+10,
			sticky='w'
		)
		hardiness_slider.grid(
			column=self.x,
			row=self.y+20,
			sticky='w'
		)
		tk.Label(
			root,
			text=(right)
			).grid(row=self.y+20, column=self.x + 20)

	

animal1 = AnimalSettings("", 10, 0, "weak", "tough")
animal2 = AnimalSettings("BOAR", 10, 10, "low reproduction", "high reproduction")

animal3 = AnimalSettings("", 10, 30, "weak", "tough")
animal4 = AnimalSettings("HOG", 10, 40, "low reproduction", "high reproduction")

def addAnimal(add_button, x, y):

    Text = font.Font(family = 'Lemon Milk',size=8) 

    def submitCommand():
        print("Haha")

    add_button = Button(root, text = "add", height = 3, width = 5, font =Text,bg='red', command=submitCommand)

    add_button.grid(
			column=x,
			row=y,
			sticky='s')

    

def deleteAnimal(del_button, x, y):

    Text = font.Font(family = 'Lemon Milk',size=8) 

    def submitCommand():
        print("Haha")

    del_button = Button(root, text = 'Delete', height = 3, width = 5, font =Text,bg='blue', command=submitCommand)

    del_button.grid(
			column=x,
			row=y,
			sticky='s')

    





def colorAnimal(button_num, x, y):
    def chooseColor():

        hex_value = colorchooser.askcolor(title = 'Pick A Color')
        real_hex_value = hex_value[1]
        print(real_hex_value)
    Text = font.Font(family = 'Lemon Milk',size=20)
    button_num = Button(root, text = 'Select Color',font = Text, command = chooseColor)
    button_num.grid(
			column=x,
			row=y,
			sticky='e')

    

addAnimal("addbutton1", 30, 10)
deleteAnimal("delbutton1", 35, 10)
colorAnimal("colorbutton1", 50, 20)

addAnimal("addbutton2", 30, 40)
deleteAnimal("delbutton2", 35, 40)
colorAnimal("colorbutton2", 50, 50)



#Dictionary


root.mainloop()

