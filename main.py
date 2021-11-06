def rot(num):
    list1 = list(num)
    a = 0
    for i in list1:
        if list1[a] == '9':
            a += 1
        elif list1[a] == '6':
            list1[a] = '9'
            break
    print(''.join(list1))
rot(num)


