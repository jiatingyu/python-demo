import random

# 随机选择一个元素
item = random.choice(['apple', 'banana', 'cherry'])
print(f"随机选择的水果: {item}")

print(f'{random.random() }') # 返回从区间[0.0, 1.0)随机抽取的浮点数

# 随机打乱列表
list_to_shuffle = [1, 2, 3, 4, 5]
random.shuffle(list_to_shuffle)
print(f"打乱后的列表: {list_to_shuffle}")

# 设置随机数生成器的种子 ， 设置随机种子后，是每次运行 文件的输出结果都一样
print(f'{random.seed(0)}')
print(f'{random.random() * 1000}')
print(f'{random.random() * 1000}')