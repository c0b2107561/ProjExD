import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo(num, f"[{num}]ボタンが押されました")

root = tk.Tk()
root.title("練習問題")
root.geometry("300x500")

r, c =0, 0
for i, num in enumerate(range(9,-1,-1),1):
    btn = tk.Button(root, text=f"{num}", width=4, height=2, font=("Times New Roman", 30))
    btn.bind("<1>",click_number)
    btn.grid(row=r, column=c)
    c+=1
    if i%3==0:
        r+=1
        c=0 
    
root.mainloop()