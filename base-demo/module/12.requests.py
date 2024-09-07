import requests
import json

# API URL
url = 'https://jsonplaceholder.typicode.com/users/1'

# Get 请求
try:
    # 发送GET请求
    response = requests.get(url, timeout=1)
    # 检查请求是否成功
    if response.status_code == 200:
        # 打印响应内容
        #print(response.text)
        # 以JSON格式解析响应内容
        print(response.json())
        user = response.json()  # 将响应内容解析为JSON
        print("查询到的用户信息：")
        print(json.dumps(user, indent=4))
    else:
        print("请求失败，状态码：", response.status_code)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError as err:
    print(f"HTTP错误: {err}")
except requests.exceptions.RequestException as err:
    print(f"请求出错: {err}")


# Post 请求
# # 用户数据
# new_user = {
#     "name": "张三",
#     "username": "zhangsan",
#     "email": "zhangsan@example.com"
# }
#
# # 发送POST请求
# response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user)
#
# # 检查请求是否成功
# if response.status_code == 201:
#     created_user = response.json()  # 获取创建后的用户信息
#     print("创建的用户信息：")
#     print(json.dumps(created_user, indent=4))
# else:
#     print("创建失败，状态码：", response.status_code)

# put 请求
# updated_user = {
#     "name": "张三",
#     "username": "zhangsan_updated",
#     "email": "zhangsan_updated@example.com"
# }
#
# # 发送PUT请求
# response = requests.put('https://jsonplaceholder.typicode.com/users/1', json=updated_user)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     updated_user_info = response.json()  # 获取更新后的用户信息
#     print("更新后的用户信息：")
#     print(json.dumps(updated_user_info, indent=4))
# else:
#     print("更新失败，状态码：", response.status_code)


# 发送DELETE请求
# response = requests.delete('https://jsonplaceholder.typicode.com/users/1')
#
# # 检查请求是否成功
# if response.status_code == 200:
#     print("用户删除成功")
# else:
#     print("删除失败，状态码：", response.status_code)



# session
#
# # 创建一个Session对象
# session = requests.Session()
#
# # 假设我们首先访问一个页面，该页面设置了一个cookie
# # httpbin.org/cookies 会返回一个设置了cookie的响应
# set_cookie_url = 'https://httpbin.org/cookies/set?sessioncookie=test'
#
# # 发送GET请求，服务器将设置cookie
# response = session.get(set_cookie_url)
#
# # 打印Session中的所有cookie
# print("Session中的Cookie:")
# for cookie in session.cookies:
#     print(cookie.name, cookie.value)
#
# # 现在访问另一个页面，Session会自动携带cookie
# headers_url = 'https://httpbin.org/headers'
#
# # 发送GET请求，查看请求头中的cookie
# response = session.get(headers_url)
# print("\n受保护页面的响应中的Cookie:")
# print(f'返回的header {response.text}')
# print(f'cookie:{response.json()['headers']['Cookie']}')  # 打印服务器接收到的Cookie