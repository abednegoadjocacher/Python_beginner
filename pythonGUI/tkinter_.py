import tkinter as tk

#tk._test() #This is to check for the version of tkinter

root = tk.Tk()
root.title("Simple App")

button = tk.Button(root,text="Button")
button.grid()

root.mainloop()
