import tkinter as tk
from tkinter import Canvas, ttk

root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Slider Demo')

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())


    


    # label for the slider
slider_label = ttk.Label(
    root,
    text='animal'
)
slider_label.grid(
    column=0,
    row=0,
    sticky='we'
)

def printval(event):
    value_label.configure(text=get_current_value())
    scalenum=round(current_value.get())
    print(scalenum)

#  slider
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    variable=current_value,
    command=printval
)


value_label = ttk.Label(
    root,
    text=get_current_value()
)

value_label.grid(
    row=3,
    columnspan=10,
    sticky='e'
)


slider.grid(
    column=1,
    row=0,
    sticky='we'
)


root.mainloop()




