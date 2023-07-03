# https://goodthings4me.tistory.com/552
# tkinter는 button위젯, text위젯, frame위젯 등 모든 것이 위젯이다.
from tkinter import *

root = Tk()
# tkinter 모듈의 Tk() 호출

btn1 = Button(root, text='Click1')
btn1.pack()

btn2 = Button(root, text='Click2', state=DISABLED)
btn2.pack()

btn3 = Button(root, text='Click3', padx=50)
btn3.pack()

btn4 = Button(root, text='Click4', padx=50, pady=50)
btn4.pack()

def clickEvent():
    label1 = Label(root, text="버튼을 클릭했네요~")
    label1.pack()

btn5 = Button(root, text="Click", fg="blue", bg="orange", command=clickEvent)
btn5.pack()

# label4 = Label(root, text='테스트 라벨 위젯 4')
# label5 = Label(root, text='테스트 라벨 위젯 5')
# label6 = Label(root, text='테스트 라벨 위젯 6')

# label4.grid(row=0, column=1)
# label5.grid(row=0, column=2)
# label6.grid(row=1, column=0)

mainloop()