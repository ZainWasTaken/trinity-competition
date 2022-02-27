from tkinter import *
import tkinter.font as font
from tkinter import colorchooser


def addAnimal():
    mainWindow = Tk()

    Text = font.Font(family = 'Lemon Milk',size=20) 
    mainWindow.geometry('300x400')

    def submitCommand():
        print("Haha")

    addButton = Button(mainWindow, text = 'Add 1', height = 3, width = 4, font =Text,bg='blue', command=submitCommand)

    addButton.pack()

    mainWindow.mainloop()

def deleteAnimal():
    mainWindow = Tk()

    Text = font.Font(family = 'Lemon Milk',size=11) 
    mainWindow.geometry('300x400')

    def submitCommand():
        print("Haha")

    deleteButton = Button(mainWindow, text = 'Remove 1', height = 4, width = 4, font =Text,bg='blue', command=submitCommand)

    deleteButton.pack()

    mainWindow.mainloop()





def colorAnimal():
    def chooseColor():

        hex_value = colorchooser.askcolor(title = 'Pick A Color')
        real_hex_value = hex_value[1]
        print(real_hex_value)
    colorWindow = Tk()
    colorWindow.geometry("300x400")
    Text = font.Font(family = 'Lemon Milk',size=20)

    colorButton = Button(colorWindow, text = 'Select Color',font = Text, command = chooseColor)
    colorButton.pack()

    colorWindow.mainloop()


colorAnimal()


#Dictionary
