filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    word_num = contents.lower().count('the')
    print('There is ' + str(word_num) + ' \'the\' in ' + filename)
