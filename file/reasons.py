

with open('reason.txt', 'w') as file_object:
    reason = input('Why you like programming: ')
    while reason != '':
        file_object.write(reason + '\n')
        reason = input('Why you like programming: ')
