# import tkinter as tk
#
# root = tk.Tk()
#
# # 水平布局
# label1 = tk.Label(root, text="Left")
# label1.pack(side="left")
#
# label2 = tk.Label(root, text="Right")
# label2.pack(side="right")
#
# # 垂直布局
# button1 = tk.Button(root, text="Top")
# button1.pack(side="top")
#
# button2 = tk.Button(root, text="Bottom")
# button2.pack(side="bottom")
#
# root.mainloop()

# 网格布局
import tkinter as tk

root = tk.Tk()

# 创建一个 3x3 网格
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=f"Button {i},{j}")
        button.grid(row=i, column=j)

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

# 绝对位置
label1 = tk.Label(root, text="Absolute Position")
label1.place(x=50, y=50)

# 相对位置
label2 = tk.Label(root, text="Relative Position")
label2.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
