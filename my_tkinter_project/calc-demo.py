import math
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("计算器")
root.geometry("400x400")

# 创建输入框
entry = tk.Entry(root, borderwidth=2, width=30, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# 计算器的逻辑部分
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

# 按钮点击事件
def on_button_click(character):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + character)

# 清除屏幕
def clear_screen():
    entry.delete(0, tk.END)

# 计算结果
def calculate_result():
    result = calculate(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)



# 创建按钮
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '', '0', '', '+',
]

rows = 4
columns = 4

for i, btn in enumerate(buttons):
    button = tk.Button(root, text=btn,width=2, font=('Arial', 18), command=lambda character=btn: on_button_click(character))
    button.grid(row= math.floor( i/rows)+1, column=i % columns, padx=10, pady=10)

# 创建特殊按钮
clear_button = tk.Button(root, text="C", font=('Arial', 18), width=2, command=clear_screen)
clear_button.grid(row=4, column=0, padx=10, pady=10)

equals_button = tk.Button(root, text='=', font=('Arial', 18), width=2, command=calculate_result)
equals_button.grid(row=4, column=2, padx=10, pady=10)

# 启动事件循环
root.mainloop()
