import tkinter as tk
from tkinter import Canvas, ttk

root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Slider Demo')


#animal values
Lion_current_value = tk.DoubleVar()
Zebra_current_value = tk.DoubleVar()
Vulture_current_value = tk.DoubleVar()
Grass_current_value = tk.DoubleVar()

#animal labels
Lion_slider_label = ttk.Label(
    root,
    text='Lion'
)
Zebra_slider_label = ttk.Label(
    root,
    text='Zebra'
)
Vulture_slider_label = ttk.Label(
    root,
    text='Vulture'
)
Grass_slider_label = ttk.Label(
    root,
    text='Grass'
)

#Slider Label Locations
Lion_slider_label.grid(
    column=0,
    row=0,
    sticky='we'
)
Zebra_slider_label.grid(
    column=0,
    row=5,
    sticky='we'
)
Vulture_slider_label.grid(
    column=0,
    row=10,
    sticky='we'
)
Grass_slider_label.grid(
    column=0,
    row=15,
    sticky='we'
)

#Slider Change Event
def Lion_get_current_value():
    return '{: .2f}'.format(Lion_current_value.get())
def Zebra_get_current_value():
    return '{: .2f}'.format(Zebra_current_value.get())
def Vulture_get_current_value():
    return '{: .2f}'.format(Vulture_current_value.get())
def Grass_get_current_value():
    return '{: .2f}'.format(Grass_current_value.get())

#Find/Map Animal Sliders
def Lion_printval(event):
    Lion_value_label.configure(text=Lion_get_current_value())
    scalenum=round(Lion_current_value.get())
    print(scalenum)
def Zebra_printval(event):
    Zebra_value_label.configure(text=Zebra_get_current_value())
    scalenum=round(Zebra_current_value.get())
    print(scalenum)
def Vulture_printval(event):
    Vulture_value_label.configure(text=Vulture_get_current_value())
    scalenum=round(Vulture_current_value.get())
    print(scalenum)
def Grass_printval(event):
    Grass_value_label.configure(text=Grass_get_current_value())
    scalenum=round(Grass_current_value.get())
    print(scalenum)

#Animal Sliders
Lion_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    variable=Lion_current_value,
    command=Lion_printval
)
Zebra_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    variable=Zebra_current_value,
    command=Zebra_printval
)
Vulture_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    variable=Vulture_current_value,
    command=Vulture_printval
)
Grass_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    variable=Grass_current_value,
    command=Grass_printval
)

#Animal Number Label
Lion_value_label = ttk.Label(
    root,
    text=Lion_get_current_value()
)
Zebra_value_label = ttk.Label(
    root,
    text=Zebra_get_current_value()
)
Vulture_value_label = ttk.Label(
    root,
    text=Vulture_get_current_value()
)
Grass_value_label = ttk.Label(
    root,
    text=Grass_get_current_value()
)

#Location for number and Slider
#LION
Lion_value_label.grid(
    row=3,
    columnspan=10,
    sticky='e'
)
Lion_slider.grid(
    column=1,
    row=0,
    sticky='we'
)
#ZEBRA
Zebra_value_label.grid(
    row=8,
    columnspan=10,
    sticky='e'
)
Zebra_slider.grid(
    column=1,
    row=5,
    sticky='we'
)
#VULTURE
Vulture_value_label.grid(
    row=13,
    columnspan=10,
    sticky='e'
)
Vulture_slider.grid(
    column=1,
    row=10,
    sticky='we'
)
#GRASS
Grass_value_label.grid(
    row=18,
    columnspan=10,
    sticky='e'
)
Grass_slider.grid(
    column=1,
    row=15,
    sticky='we'
)

tk.Label(
    root,
    text="New Species:"
    ).grid(row=0, column=30)

new_animal = tk.Entry(root)
new_animal.grid(row=0, column=40)

root.mainloop()