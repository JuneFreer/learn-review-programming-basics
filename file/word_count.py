def count_words(filename): # 形参/占位符
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError: # 处理文件不存在的情况
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')
        # Python会在print函数后自动加一个\n

# filename = 'alice.txt' # 实参
# count_words(filename) # 调用函数count_words，传入参数


# 统计多个文件的字数
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename) #在文件列表中遍历文件，并传给count_words()作实参
