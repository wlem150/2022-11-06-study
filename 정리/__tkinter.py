import calendar

c = calendar.TextCalendar()
m = c.formatmonth(2021,2)
print(m)

import tkinter
import calendar
a = tkinter.Tk()
t = tkinter.Text(a,width=10, height=10)
a.pack()
tkinter.mainloop()


# import tkinter as tk

# s = "Life is short\nUse Python"

# root = tk.Tk()
# t = tk.Text(root, height=10, width=10)
# t.insert(tk.END, s)
# t.pack()
# tk.mainloop()

import tkinter

window = tkinter.Tk()
window.title("SampleTitle")
window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text="Sample")
label.pack()
window.mainloop()

"""
변수 = tkinter.Tk()

를 이용하여 가장 상위 레벨의 윈도우 창을 생성할 수 있다.


변수 = mainloop()

윈도우 창을 종료할 때까지 실행할 수 있다.


변수 = geometry("너비x높이+x좌표+y좌표") 

윈도우 창의 너비와 높이, 초기 화면 위치의 x좌표와 y좌표를 설정할 수 있다.


변수 = resizable(상하, 좌우)

윈도우 창의 창 크기 조절 기능 여부를 설정할 수 있다.
True 로 설정할 경우 윈도우 창의 크기를 조절할 수 있다.

True == 1, False == 0 과 같기 때문에, 상수를 입력해도 상관없다.


변수 = tkinter.Label(window, text="입력값")

윈도우창에 입력값을 출력할 수 있다.


위젯.pack()

위젯을 배치할 수 있다.
"""


