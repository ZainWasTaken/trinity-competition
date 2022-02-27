import tkinter as tk
from tkinter import ttk

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
    sticky='w'
)

def printval(event):
    scalenum=current_value.get()
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

current_value_label = ttk.Label(
    root,
    text='Current Value:'
)
slider.grid(
    column=1,
    row=0,
    sticky='we'
)


root.mainloop()




