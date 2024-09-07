# # 基本使用
#
# from multiprocessing import Process
# import os
# def worker(name , addr):
#     print(f'Worker: {name } {addr}, 父进程pid {os.getppid()}')
#
# if __name__ == '__main__':
#     print(f'系统pid {os.getpid()}')
#     p = Process(target=worker, args=('新进程','未知'))
#     p.start()
#     p.join()


# # 进程池
#
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print(f'运行任务 {name} {os.getpid()}')
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('PID %s.' % os.getpid())
#     p = Pool(4) # 开启4个进程池
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,)) # 添加 5 个同步任务 ， 就会出现任务等待情况
#     print('等到所有子进程执行结束...')
#     p.close() # 调用close()之后就不能继续添加新的Process了。
#     p.join()
#     print('所有进程执行结束')


# import subprocess
#
# print('$ ping www.baidu.com')
# r = subprocess.call(['ping', 'www.baidu.com'])
# print('Exit code:', r)


from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
