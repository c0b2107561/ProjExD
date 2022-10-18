import tkinter as tk
import maze_maker as mn  #練習8

def key_down(event): #練習5-1
    global key
    key = event.keysym

def key_up(event): #練習6-1
    global key
    key = " "

def main_proc(): #練習7　#練習11
    global mx, my
    global cx, cy
    if key == "Up":
        my -=1
    if key == "Down":
        my +=1
    if key == "Left":
        mx -=1
    if key == "Right":
        mx +=1
    cx, cy = mx*100+50, my*100+50

    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack() #練習2

    maze_lst = mn.make_maze(15,9) #1:壁、0:床 #練習9

    mn.show_maze(canvas, maze_lst)#練習10


    tori = tk.PhotoImage(file="ex03/fig/4.png")
    mx, my = 1, 1 #練習11
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori") #練習3

    key = "" #現在押されているキーを表す #練習4

    root.bind("<KeyPress>",key_down) #練習5-2
    root.bind("<KeyRelease>", key_up) #練習6-2

    main_proc() #練習7

    
    root.mainloop()