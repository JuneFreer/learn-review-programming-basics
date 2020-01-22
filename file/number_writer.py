import json # 引入json库

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj) # 用json.dump()把列表numbers写入文件对象f_obj，dump()是json库中的函数，可以被json调用
    
