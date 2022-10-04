import tkinter as tk
import tkinter.messagebox as tkm


def click_number(event):#練習3
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num) #練習5

def click_equal(event):#四則演算
    eqn = entry.get() #引数いらない。空にする。
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res) #練習7

def click_allclear(evnt):#全削除
    eqn = entry.get()
    entry.delete(0, tk.END)

def click_clear(event):#1文字削除
    eqn = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0,eqn[:-1])

def click_equals(event):#%表示
    eqn=entry.get()
    res=eval(eqn)/100
    entry.delete(0, tk.END)
    entry.insert(0, res)
    

root = tk.Tk()
root.title("練習問題")
root.geometry("400x750")

entry = tk.Entry(root, width=10, font=("",40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 #rは行、cは列を表す変数
numbers = list(range(9,-1,-1)) #数字だけのリスト
operators = ["+","-","*","/"] #演算子だけのリスト

for i, num in enumerate(numbers+operators,1):
    btn = tk.Button(root, text=f"{num}", width=4, height=2, font=("Times New Roman", 30))
    btn.bind("<1>",click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn = tk.Button(root, text=f"=", width=4, height=2, font=("Times New Roman", 30))
btn.bind("<1>", click_equal)
btn.grid(row=r-2, column=c+1)

btn = tk.Button(root, text=f"AC", width=4, height=2, font=("Times New Roman", 30))
btn.bind("<1>", click_allclear)
btn.grid(row=r-1, column=c+1)

btn = tk.Button(root, text=f"C", width=4, height=2, font=("Times New Roman", 30))
btn.bind("<1>", click_clear)
btn.grid(row=r, column=c+1)

btn = tk.Button(root, text=f"%", width=4, height=2, font=("Times New Roman", 30))
btn.bind("<1>", click_equals)
btn.grid(row=r, column=c)

root.mainloop()