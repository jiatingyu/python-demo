import mypackage

import atexit

def cleanup():
    print("执行清理工作...")

def main():
    print("程序开始执行。")
    # 注册清理函数
    atexit.register(cleanup)

    # 程序主逻辑 ---
    print(mypackage.hello())
    print(mypackage.hello2())


if __name__ == "__main__":
    main()

