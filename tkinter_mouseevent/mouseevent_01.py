from tkinter import *
from PIL import ImageGrab

x1 = y1 = x2 = y2 = 0

def clicked(event):
    global x1, y1
    x1, y1 = event.x, event.y

def released(event):
    global x2, y2
    x2, y2 = event.x, event.y
    canvas.create_line(x1, y1, x2, y2, width=3)

def save():
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    w = window.winfo_width() + x
    h = window.winfo_height() + y

    box = (x, y, w, h)
    img = ImageGrab.grab(box)
    saveas = "capture.png"
    img.save(saveas)

window = Tk()

label = Label(window, text="캔버스 그림판", font=("나눔글꼴", 30, "bold"))
label.pack(pady=30)

savebutton = Button(window, text="SAVE", fg="blue", font=("나눔명조", 10), command=save)
savebutton.pack()

canvas = Canvas(window, width=500, height=500, bg="yellow", relief="ridge", bd=5)
canvas.pack(pady=30)

canvas.bind("<Button>", clicked)
canvas.bind("<ButtonRelease>", released)

window.mainloop()
