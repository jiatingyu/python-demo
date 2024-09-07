# import threading
#
# def print_numbers():
#     for i in range(1, 6):
#         print(f'当前线程{threading.current_thread().name} , 输出值 {i}')
#
# thread = threading.Thread(target=print_numbers)
# thread.start()
# thread.join()
# print(f'默认主线程 {threading.current_thread().name} 执行完毕')



# 多线程
import time,threading
#
# balance = 0
# lock = threading.Lock()
# def add_numbers():
#     for i in range(1, 100000):
#         try:
#             # lock.acquire()
#             global balance
#             balance += i
#             balance -= i
#             print(f'Thread {threading.current_thread().name}: 计算次数 {i} , 余额：{balance}')
#         finally:
#             # lock.release()
#             print()
# # def sub_numbers():
# #     for i in range(1, 10000):
# #         try:
# #             # lock.acquire()
# #             global balance
# #             balance -= i
# #             print(f'Thread {threading.current_thread().name}: 计算次数 {i} , 余额：{balance}')
# #         finally:
# #             # lock.release()
# #             print()
#
# t1 = threading.Thread(target=add_numbers, name='计算器1')
# t2 = threading.Thread(target=add_numbers, name='计算器2')
# t1.start()
# t2.start()
# # t1.join()
# # t2.join()
#
# print(balance)

# # 共享计数器
# counter = 0
#
# def increment():
#     global counter
#     for _ in range(100000):
#         counter += 1
#
# # 创建两个线程
# thread1 = threading.Thread(target=increment)
# thread2 = threading.Thread(target=increment)
# thread3 = threading.Thread(target=increment)
#
# # 启动线程
# thread1.start()
# thread3.start()
# thread2.start()
#
# # 等待线程完成
# thread1.join()
# thread2.join()
# thread3.join()
#
# print(f"Expected counter value: 200000")
# print(f"Actual counter value: {counter}")

import threading

# 共享文件对象

balance = 0
def write_to_file(thread_id):
    for _ in range(10):  # 每个线程写入10000次
        global balance
        balance+=1
        file = open('shared.txt', 'w')
        file.write(f"{balance },_name")
        file.close()

# 创建多个线程
threads = []
for i in range(10):  # 创建10个线程
    thread = threading.Thread(target=write_to_file, args=(i,))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

file.close()
