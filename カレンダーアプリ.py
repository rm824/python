import tkinter as tk
import calendar as cl

def pre_month():
    global y
    global m

    if m == 1:
        m = 12
        y = y - 1
    else:
         m = m - 1
         
    lbl.configure(text=cl.month(y,m))

def add_month():
    global y
    global m

    if m == 12:
        m = 1
        y = y + 1
    else:
        m = m + 1
    
    lbl.configure(text=cl.month(y,m))

root = tk.Tk()
root.geometry("300x200")
root.title("カレンダー")

y=2021
m=4

# ラベル
lbl = tk.Label(text=cl.month(y,m))

lbl.pack()

# ボタン
btn1 = tk.Button(text="←",command=pre_month)
btn2 = tk.Button(text="→",command=add_month)

btn1.place(x=100,y=150)
btn2.place(x=150,y=150)




tk.mainloop()
