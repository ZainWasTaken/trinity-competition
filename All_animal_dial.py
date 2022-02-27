from distutils import command
import tkinter as tk
from tkinter import Canvas, ttk, font


root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)
<<<<<<< Updated upstream
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
=======
root.title("Slider Demo")
textFont = font.Font(family="Lemon Milk", size=20)
>>>>>>> Stashed changes


class AnimalDisplay:
    def __init__(self, label: str, number: int, root):
        self.current_value = tk.DoubleVar()
        self.slider_label = ttk.Label(root, text=label)
        self.slider_label.grid(column=0, row=number * 5, sticky="we")
        self.value_label = ttk.Label(root, text=self.get_current_value())
        self.slider = ttk.Scale(
            root,
            from_=0,
            to=100,
            orient="horizontal",  # vertical
            variable=self.current_value,
            command=self.eval,
        )
        self.value_label.grid(row=3 + 5 * number, columnspan=10, sticky="e")
        self.slider.grid(column=1, row=5 * number, sticky="e")

    def get_current_value(self) -> str:
        return "{: .2f}".format(self.current_value.get())

    def eval(self, event: str):
        self.slider_label = ttk.Label(root, text=self.get_current_value())


raw = ["Lion", "Zebra", "Vulture", "Grass"]

num = 0
disps = []


def add_new_animal(name):
    global num, root
    disps.append(AnimalDisplay(name, num, root))
    num += 1


for name in raw:
    add_new_animal(name)


def add_animal_from_new_button():
    add_new_animal(new_animal.get())


tk.Label(root, text="New Species:").grid(row=0, column=30)

new_animal = tk.Entry(root)
new_animal.grid(row=0, column=40)

new_animal_btn = tk.Button(
    root, text="Add New Animal", command=add_animal_from_new_button
)
new_animal_btn.grid(column=0, row=num * 5, sticky="we")

root.mainloop()
