s = "Hello, World!"
print(s[0])  # 输出: H
print(s[7])  # 输出: W


print(s.find('o'))
print(s.index('o'))
print(s.count('o'))
print(s.startswith('o'))
print(s.endswith('o'))


print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace('o','K'))

print(s[1:2])
print(s[1:])
print(s[:2])

print(3*3)
print(3**3)

a = True
b= False
c=10
print(  a & c)

name = "张胜男"
age = 30
print("Hello, %s. You are %d years old." % (name, age))
