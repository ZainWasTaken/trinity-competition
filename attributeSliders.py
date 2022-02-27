import tkinter as tk
import tkinter.font as font
from tkinter import Canvas, ttk

root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Slider Demo')


#animal values
class AnimalSettings:
	def __init__(self, name, x, y):	
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
			sticky='we'
		)
		#animal labels
		hardiness_slider_label = ttk.Label(
			root,
			text='Weak'
		)


		#Slider Label Locations
		hardiness_slider_label.grid(
			column=self.x+50,
			row=self.y+20,
			sticky='we'
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
			sticky='e'
		)
		hardiness_slider.grid(
			column=self.x + 1,
			row=self.y+20,
			sticky='we'
		)
		tk.Label(
			root,
			text="Tough"
			).grid(row=self.y+20, column=self.x + 30)

	

animal1 = AnimalSettings("boar", 0, 0)
root.mainloop()
