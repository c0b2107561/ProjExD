import tkinter as tk
import maze_maker as mn  #練習8
import random
import tkinter.messagebox

def key_down(event): #練習5-1
    global key
    key = event.keysym

def key_up(event): #練習6-1
    global key
    key = " "

def main_proc(): #練習7　#練習11
    global mx, my #マス
    global cx, cy #座標
    global yuka
    if key == "Shift_L" and yuka > 1: #左のシフトを押すとやり直し
        mx = 1 #キャラクターを初期位置に移動
        my = 1 #キャラクターを初期位置に移動
        yuka = 0 #床を塗った数を初期化
        for y in range(7): #床を塗った数を初期化
            for x in range(10):
                if maze_lst[y][x] == 2:
                    maze_lst[y][x] = 0
    if key == "Up" and maze_lst[my-1][mx] == 0:
        my -= 1
    if key == "Down" and maze_lst[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze_lst[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze_lst[my][mx+1] == 0:
        mx += 1
    if maze_lst[my][mx] == 0:
        maze_lst[my][mx] = 2
        yuka = yuka + 1
        canvas.create_rectangle(mx*100,my*100,mx*100+100,my*100+100,fill="pink") #タグづけして一度に全て削除
    canvas.delete("koukaton") #キャラを消す
    canvas.create_image(mx*100+50, my*100+50, image=tori, tag="koukaton") #キャラを再描写
    root.after(100,main_proc)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack() #練習2

    maze_lst = mn.make_maze(15,9) #1:壁、0:床 #練習9

    mn.show_maze(canvas, maze_lst)#練習10
    
    canvas.create_rectangle(1300, 700, 1400, 800,fill="yellow")
    canvas.create_text(1350, 750, text="GOOL!",font=(None,25), fill="red")


    tori = tk.PhotoImage(file="ex03/fig/4.png")
    mx, my = 1, 1 #練習11
    yuka = 0 #yukaの初期値
    cx, cy = 300, 400


    key = "" #現在押されているキーを表す #練習4

    root.bind("<KeyPress>",key_down) #練習5-2
    root.bind("<KeyRelease>", key_up) #練習6-2

    main_proc() #練習7

    
    root.mainloop()