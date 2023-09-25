##n = int(input('Введите число от 0 до 31'))
##if n < 0 or n = 31:
##    print('Некорректные данные')
##else:
##    s = '1'
##n //= 2
##    if n % 2 == 0:
##    s = '0' + s
##    else:
##        s = '1'
##        n //= 2

n = int(input('Введите число от до 31 '))
if 0 <= n <= 31:
    s = ' '
    s = str(n % 2) + s
    n //= 2
    s = str(n % 2) + s
    n //= 2
    s = str(n % 2) + s
    n //= 2
    s = str(n % 2) + s
    n //= 2
    s = str(n % 2) + s
    print('Результат = ', s)
else:
    print('Некорректные данные')
    
