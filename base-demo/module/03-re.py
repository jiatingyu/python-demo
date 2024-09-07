import re

text = 'Hello world!'

res = re.match(r"(\w|\s)+", text)
print(res)
if res:
    print('成功匹配')
else:
    print('未匹配到')

# 搜索数字
match = re.search(r'\d+', '这里有123个苹果')
print(f"搜索到的数字: {match.group()}")

# 替换字符串中的单词
replaced = re.sub(r'苹果', '橙子', '我买了3个苹果')
print(f"替换后的字符串: {replaced}")

# 匹配邮箱地址
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', '请联系example@example.com或test@example.net')
print(f"找到的邮箱地址: {emails}")