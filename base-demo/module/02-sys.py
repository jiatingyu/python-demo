import sys

# 打印命令行参数
print(f"命令行参数: {sys.argv}")

# 获取Python解释器的路径
print(f"Python解释器路径: {sys.executable}")

# 设置并获取最大递归深度
sys.setrecursionlimit(1000)
print(f"最大递归深度: {sys.getrecursionlimit()}")