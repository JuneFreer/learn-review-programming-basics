import json
"""使用json.load()将这个列表读取到内存中"""

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj) # 我们使用函数json.load()加载存储在numbers.json中的信息， 并将其存储到变量numbers中

print(numbers)
