from tkinter import *

window = Tk()

# relief_list = ["flat", "groove", "raised", "ridge", "solid", "sunken"]
# for i in range(len(relief_list)):
#     Label(window, text=relief_list[i], relief=relief_list[i], font=("나눔명조", 20, "bold")).pack()

canvas = Canvas(window, width=500, height=500, bg="pink")
canvas.pack()

window.mainloop()