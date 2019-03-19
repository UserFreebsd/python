a=int(input())
b=int(input())
if b != 0:
    print (a/b)
else:
    print('Введите не 0')
    b=int(input('Введите не нулевое значение'))
    if b == 0:
        print('Введите 0')
    else:
        print(a/b)

