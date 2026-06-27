import tkinter as tk
from tkinter import messagebox, simpledialog
import random

def computer():
    global number
    down_number = 1
    up_number = 10000
    while True:
        player = "0"
        try:
            is_player = True
            while is_player:
                player = simpledialog.askstring("输入", f"输入一个{down_number}～{up_number}的数字")
                if player.strip() == "":
                    messagebox.showwarning("警告", "你没有输入任何内容")
                else:
                    try:
                        temp = int(player)
                    except:
                        messagebox.showwarning("警告", "你输入的不是数字")
                    else:
                        if int(player) > up_number:
                            messagebox.showwarning("警告", "你输入的数字大于了上限")
                        elif int(player) < down_number:
                            messagebox.showwarning("警告", "你输入的数字小于了下限")
                        else:
                            is_player = False
        except:
            if messagebox.askyesno("询问", "是否退出"):
                break
        if int(player) == number:
            messagebox.showinfo("结果", "Boom！你猜中了，你输了")
            break
        if int(player) > number:
            up_number = int(player) - 1
        if int(player) < number:
            down_number = int(player) + 1

        computer = random.randint(down_number, up_number)
        messagebox.showinfo("电脑输入", f"电脑输入了{computer}")
        if computer == number:
            messagebox.showinfo("结果", "Boom！电脑猜中了，你赢了")
            break
        if computer > number:
            up_number = int(computer) - 1
        if computer < number:
            down_number = int(computer) + 1

def people():
    global number
    down_number = 1
    up_number = 10000
    while True:
        player1 = "0"
        try:
            is_player = True
            while is_player:
                player1 = simpledialog.askstring("输入", f"输入一个{down_number}～{up_number}的数字")
                if player1.strip() == "":
                    messagebox.showwarning("警告", "玩家1没有输入任何内容")
                else:
                    try:
                        temp = int(player1)
                    except:
                        messagebox.showwarning("警告", "玩家1输入的不是数字")
                    else:
                        if int(player1) > up_number:
                            messagebox.showwarning("警告", "玩家1输入的数字大于了上限")
                        elif int(player1) < down_number:
                            messagebox.showwarning("警告", "玩家1输入的数字小于了下限")
                        else:
                            is_player = False
        except:
            if messagebox.askyesno("询问", "是否退出"):
                break
        if int(player1) == number:
            messagebox.showinfo("结果", "Boom！玩家1猜中了，玩家1输了")
            break
        if int(player1) > number:
            up_number = int(player1) - 1
        if int(player1) < number:
            down_number = int(player1) + 1

        player1 = "0"
        try:
            is_player = True
            while is_player:
                player1 = simpledialog.askstring("输入", f"输入一个{down_number}～{up_number}的数字")
                if player1.strip() == "":
                    messagebox.showwarning("警告", "玩家2没有输入任何内容")
                else:
                    try:
                        temp = int(player1)
                    except:
                        messagebox.showwarning("警告", "玩家2输入的不是数字")
                    else:
                        if int(player1) > up_number:
                            messagebox.showwarning("警告", "玩家2输入的数字大于了上限")
                        elif int(player1) < down_number:
                            messagebox.showwarning("警告", "玩家2输入的数字小于了下限")
                        else:
                            is_player = False
        except:
            if messagebox.askyesno("询问", "是否退出"):
                break
        if int(player1) == number:
            messagebox.showinfo("结果", "Boom！玩家2猜中了，玩家2输了")
            break
        if int(player1) > number:
            up_number = int(player1) - 1
        if int(player1) < number:
            down_number = int(player1) + 1


def how_to_play():
    messagebox.showinfo("玩法说明", "会有一个在1～10000之间的随机数，你们两个需要轮流猜，猜中就输了")

def on_closing():
    global root, game_loop
    game_loop = False
    root.destroy()

game_loop = True
while game_loop:
    number = random.randint(1, 10000)
    root = tk.Tk()

    root.title("选择")

    width = 200
    height = 120

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

    tablet = tk.Label(root, text="选择模式")
    tablet.pack()

    button1 = tk.Button(root, text="电脑对战", command=computer)
    button1.pack()

    button2 = tk.Button(root, text="双人对战", command=people)
    button2.pack()

    button3 = tk.Button(root, text="玩法说明", command=how_to_play)
    button3.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

