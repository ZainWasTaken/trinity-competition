from tkinter import *   
  

mainWindow = Tk()  
  

mainWindow.geometry('300x400')  
    
def submitCommand():
    print("Haha")
button = Button(mainWindow, text = 'click', bg='blue', command=submitCommand) 
button.pack()  
mainWindow.mainloop()

