import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj) # 把username写入文件username.json
    print("We'll remember you when you come back, " + username + "!")
