# class Person:
#     def __init__(self,*args):
#       pass
#
# # 创建 Student 类的实例
# p = Person()
# p.name = '子羽'
# print(p.name)

#
# def my_decorator(func):
#     def wrapper(world):
#         print("日志记录开始.")
#         func(world)
#         print("日志记录结束")
#     return wrapper
#
# @my_decorator
# def say_hello(world):
#     print(f"Hello {world}!")
#
# say_hello('子羽')


# 枚举示例

# from enum import Enum, auto
#
# class Color(Enum):
#     RED = auto() # 默认从 1 开始
#     GREEN = auto()
#     BLUE = auto()
#     YELLOW = 5
#     purple = 6
#
# print(Color.RED)  # 输出: Color.RED
# print(Color.GREEN.name)  # 输出: GREEN
# print(Color.GREEN.value)  # 输出: 2
# print(Color.YELLOW.name)  # 输出: YELLOW
# print(Color.YELLOW.value)  # 输出: 5


# 元类

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"创建新类 ：{name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"初始化类： {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    def __init__(self):
        print("创建 Myclass 类的示例")

obj = MyClass()
