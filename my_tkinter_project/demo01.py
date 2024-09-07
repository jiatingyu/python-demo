import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("我的 GUI 应用程序")
root.geometry("400x300")  # 设置窗口大小

# 创建一个标签
label = tk.Label(root, text="Hello, Tkinter!", font="")
label.pack(pady=20)

# 创建一个文本框
entry = tk.Entry(root)
entry.pack(pady=20)

# 创建一个按钮
button = tk.Button(root, text="点击我，输入文字")
button.pack(pady=20)




def on_button_click():
    entry.delete(0, tk.END)  # 清空文本框
    entry.insert(0, "欢迎使用 Tkinter!")

# 绑定事件处理函数到按钮点击事件
button.config(command=on_button_click)


root.mainloop()