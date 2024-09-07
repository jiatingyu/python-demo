from collections import namedtuple, deque, Counter

# 使用 namedtuple 创建一个命名元组
Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print(f"命名元组: {point}")

# 使用 deque 实现队列
queue = deque()
queue.append('right')
queue.appendleft('left')

print(f"队列: {queue}")

# 使用 Counter 进行计数
words = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
word_counts = Counter(words)
print(f"单词计数: {word_counts}")