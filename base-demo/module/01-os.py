import os

# 获取当前工作目录
current_directory = os.getcwd()
print(f"当前工作目录: {current_directory}")

# 改变当前工作目录
os.chdir('../class-demo')
print(f"改变后的工作目录: {os.getcwd()}")

# 列出目录中的文件和文件夹
entries = os.listdir('.')
print(f"目录中的条目: {entries}")

# 检查路径是否存在
path_exists = os.path.exists('../class-demo/')
print(f"路径存在: {path_exists}")

# 获取文件的大小
file_size = os.path.getsize('../class-demo/demo01.py')
print(f"文件大小: {file_size} 字节")