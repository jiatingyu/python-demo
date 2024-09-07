print("hello world")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
sum = 0
x = range(1,101)

for i in x:
    sum = sum + i
print(sum)

count = 1
while count <= 5:
    print(count)
    count += 1


for i in range(10):
    if i % 2 == 0: # 偶数就跳过，print就只会打印计数的数字
        continue
    print(i)


def make_twice(func):
    def wrapper(x):
        return func(func(x))
    return wrapper

@make_twice
def double(x):
    return x * 2

print(double(5))  # 输出: 20


def match_type(value):
    match value:
        case int():
            print("这是一个整数")
        case float():
            print("这是一个浮点数")
        case str():
            print("这是一个字符串")
        case _:
            print("未知类型")

match_type(10)  # 输出：这是一个整数
match_type(3.14)  # 输出：这是一个浮点数
match_type("hello")  # 输出：这是一个字符串
match_type([1, 2, 3])  # 输出：未知类型


def match_sequence(value):
    match value:
        case [1, 2, 3]:
            print("匹配到 [1, 2, 3]")
        case (1, num):
            print("匹配到元组，第一个元素为 1",'第二个数', num)
        case [1, *rest]:
            print(f"匹配到以 1 开头的列表，其余元素为 {rest}")
        case _:
            print("匹配到其他值")

match_sequence([1, 2, 3])  # 输出：匹配到 [1, 2, 3]
match_sequence([1, 4, 5])  # 输出：匹配到以 1 开头的列表，其余元素为 [4, 5]
match_sequence((1, 2))  # 输出：匹配到元组，第一个元素为 1 第二个数 2
match_sequence("hello")  # 输出：匹配到其他值




def match_named(value):
    match value:
        case (a, b):
            print(f"匹配到元组，第一个元素为 {a}，第二个元素为 {b}")
        case {"name": name, "age": age}:
            print(f"匹配到字典，名字为 {name}，年龄为 {age}")
        case _:
            print("匹配到其他值")

match_named((1, 2))  # 输出：匹配到元组，第一个元素为 1，第二个元素为 2
match_named({"name": "Alice", "age": 30})  # 输出：匹配到字典，名字为 Alice，年龄为 30
match_named([1, 2, 3])  # 输出：匹配到其他值


age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')


def match_sequence(value):
    match value:
        case [1, *rest]:
            print(f"匹配到以 1 开头的列表，其余元素为 {rest}")
        case _:
            print("匹配到其他值")


match_sequence([1, 2, 3])  # 输出：匹配到以 1 开头的列表，其余元素为 [2, 3]
match_sequence([1, 4, 5])  # 输出：匹配到以 1 开头的列表，其余元素为 [4, 5]

