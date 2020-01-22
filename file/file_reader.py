with open('text_files/pi_digits.txt') as file_object: #  文件对象
    cotents = file_object.read() #读取全部文件
    print(cotents.rstrip()) # 打印到屏幕/命令行
