import json

# JSON 编码
data = {'name': '子羽', 'age': 30, 'city': '成都'}
json_string = json.dumps(data)
print(f"JSON 编码: {json_string}")

# JSON 解码
decoded_data = json.loads(json_string)
print(f"JSON 解码: {decoded_data}")