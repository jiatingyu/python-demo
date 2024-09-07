
# 按钮样式
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()
style.configure('TButton', font=('Arial', 16), background='red', relief='raised',foreground="red")

button = ttk.Button(root, text='Styled Button', style='TButton')
button.pack(pady=40 ,padx=40)

root.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# style = ttk.Style()
# available_themes = style.theme_names()
# print("Available themes:", available_themes)
# # Available themes: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
#
# # 切换到 'alt' 主题
# style.theme_use('alt')
#
# button = ttk.Button(root, text='Button in Alt Theme')
# button.pack(pady=20)
#
# root.mainloop()