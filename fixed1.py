import time

b = 0
while b == 0:
    print('Введите число')
    x = int(input())

    print('Укажите знак (+, -, *, /)')
    y = input()

    print('Введите второе число')
    z = int(input())

    if   y == '+': m = x + z
    elif y == '-': m = x - z
    elif y == '*': m = x * z
    elif y == '/':
        if z == 0:
            print('Ошибка: деление на ноль')
            exit()
        m = x / z
    else:
        print('Неверный оператор')
        exit()


    print('Результат:', m)
    time.sleep(1)
    print('Хотите еще? (да/нет)')
    o = str(input())
    if o == 'нет':
        b = 1
    elif o == 'да':
        b = 0
    elif o != 'да':
        b = 1
