import tkinter as tk

def key_down(event): #練習5-1
    global key
    key = event.keysym

def key_up(event): #練習6-1
    global key
    key = " "

def main_proc(): #練習7
    global cx, cy
    if key == "Up":
        cy -=20
    if key == "Down":
        cy +=20
    if key == "Left":
        cx -=20
    if key == "Right":
        cx +=20

    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack() #練習2

    tori = tk.PhotoImage(file="ex03/fig/4.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori") #練習3

    key = "" #現在押されているキーを表す #練習4

    root.bind("<KeyPress>",key_down) #練習5-2
    root.bind("<KeyRelease>", key_up) #練習6-2

    main_proc()

    root.mainloop()