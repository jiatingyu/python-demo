from threading import Thread

# 定义线程要执行的函数
def print_numbers():
    for i in range(5):
        print(f"线程打印: {i}")

# 创建线程
thread = Thread(target=print_numbers)
thread.start()  # 启动线程

# 等待线程完成
#thread.join()
print("主线程继续执行")