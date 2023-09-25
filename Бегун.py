while True:
    s = input('Введите количество дней ')
    if s.isdigit():
        n = int(s)
        if n !=0:
            break
        else:
            print('Ошибка')
    else:
        print('Ошибка')
r = 10
for i in range(2, n +1):
    r += 0.1 * r
print(f'{n} дн. = {r} км')
    
