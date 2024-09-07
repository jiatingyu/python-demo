from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt
import sys
from PyQt6.QtWidgets import QGridLayout
import  math
rows = 4
columns = 4
class MainWindow(QMainWindow):
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '', '0', '', '+',
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT计算器")
        self.setGeometry(100, 100, 400, 300)  # 设置窗口位置和大小

        # 创建一个按钮并设置属性
        # self.button = QPushButton("点击我", self)
        # self.button.setGeometry(150, 130, 100, 30)  # 设置按钮位置和大小
        # self.button.clicked.connect(self.on_button_clicked)

        # 创建布局

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        # layout.addWidget(button1, 0, 0)  # 第0行，第0列
        # layout.addWidget(button2, 0, 1)  # 第0行，第1列
        # layout.addWidget(another_button, 1, 0)  # 第1行，第0列
        # for i, btn in enumerate(self.buttons):
        #     btxt = QPushButton(btn, self)
        #     # tk.Button(root, text=btn,width=2, font=('Arial', 18), command=lambda character=btn: on_button_click(character))
        #     # button.grid(row= math.floor( i/rows)+1, column=i % columns, padx=10, pady=10)
        #     self.layout.addWidget(btxt, math.floor(i/rows)+1, i % columns)
        #     print(math.floor(i/rows)+1, i % columns)
        # print(window)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            # if name == '':
            #     continue

            button = QPushButton(name,self)
            self.layout.addWidget(button, *position)
            print(*position, name)



    def on_button_clicked(self):
        print("按钮被点击了")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = MainWindow()
    window1.show()
    sys.exit(app.exec())

# # 创建主窗口
# root = tk.Tk()
# root.title("计算器")
# root.geometry("400x400")
#
# # 创建输入框
# entry = tk.Entry(root, borderwidth=2, width=30, font=('Arial', 18))
# entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
#
# # 计算器的逻辑部分
# def calculate(expression):
#     try:
#         result = eval(expression)
#         return str(result)
#     except Exception as e:
#         return "Error"
#
# # 按钮点击事件
# def on_button_click(character):
#     current_expression = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current_expression + character)
#
# # 清除屏幕
# def clear_screen():
#     entry.delete(0, tk.END)
#
# # 计算结果
# def calculate_result():
#     result = calculate(entry.get())
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, result)
#
#
#
# # 创建按钮
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '', '0', '', '+',
# ]
#
# rows = 4
# columns = 4
#
# for i, btn in enumerate(buttons):
#     button = tk.Button(root, text=btn,width=2, font=('Arial', 18), command=lambda character=btn: on_button_click(character))
#     button.grid(row= math.floor( i/rows)+1, column=i % columns, padx=10, pady=10)
#
# # 创建特殊按钮
# clear_button = tk.Button(root, text="C", font=('Arial', 18), width=2, command=clear_screen)
# clear_button.grid(row=4, column=0, padx=10, pady=10)
#
# equals_button = tk.Button(root, text='=', font=('Arial', 18), width=2, command=calculate_result)
# equals_button.grid(row=4, column=2, padx=10, pady=10)
#
# # 启动事件循环
# root.mainloop()

