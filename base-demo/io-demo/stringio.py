from io import StringIO,BytesIO

s = StringIO()
s.write('Hello')
s.write(' -- ')
s.write('World')
print(f'获取内存s的值：{s.getvalue()}')

# BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f'获取内存f的值：{f.getvalue()}')


# 很多时候，数据读写不一定是文件，也可以在内存中读写 , StringIO顾名思义就是在`内存中读写str`,StringIO操作的只能是str，如果要操作二进制数据，就需要使用`BytesIO`。