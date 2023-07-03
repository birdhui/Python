from tkinter import *
# PIL : 이미지 관련 처리를 해주는 라이브러리
from PIL import ImageGrab

# 초기값 지정
x1 = y1 = x2 = y2 = 0

# 마우스 클릭되었는지, 어떤 키가 눌려졌는지 확인하는 함수
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

# relief_list = ["flat", "groove", "raised", "ridge", "solid", "sunken"]
# for i in range(len(relief_list)):
#    Label(window, text=relief_list[i], relief=relief_list[i], font=("나눔바른펜", 20, "bold"), bd=5)

# 캔버스 레이블 옵션
label = Label(window, text="캔버스 그림판", font=("나눔글꼴", 30, "bold"))
# 캔버스 레이블 팩 배치, pady : 여백두기
label.pack(pady=30)

savebutton = Button(window, text="Save", fg="red", font=("나눔글꼴", 10), command=save)
savebutton.pack()

canvas = Canvas(window, width=500, height=500, bg="white", relief="ridge",bd=5)
canvas.pack()
# bind 사용해 마우스 버튼이 클릭되었는지 확인
canvas.bind("<Button>", clicked)
# 마우스 버튼을 눌렀을 때
canvas.bind("<ButtonRelease>", released)

window.mainloop()