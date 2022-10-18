import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack() #練習2

    tori = tk.PhotoImage(file="ex03/fig/4.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori") #練習3

    key = "" #現在押されているキーを表す #練習4

    root.mainloop()