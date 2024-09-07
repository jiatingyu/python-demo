# import mymodule
#
# print(mymodule.greet("张三"))
# print(mymodule.PI)
# circle = mymodule.area(5)
# print(circle)
#
# print(mymodule.__getname())

from mymodule import *

print(greet("张三"))
print(PI)



# import sys
# print(sys.path)
# sys.path.append('/path/to/my/modules')

# print(__name__)
#
# if __name__ == "__main__":
#     print("这是模块是直接被运行的")
# else:
#     print("这个模块是被导入运行的")
print(age)