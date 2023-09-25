m = int(input('Введите номер месяца '))

if m == 12 or m == 1 or m == 2:
    print('Месяц зимний')
elif m == 3 or m == 4 or m == 5:
    print('Месяц весенний')
elif m == 6 or m == 7 or m == 8:
    print('Месяц осенний')
elif m == 9 or m == 10 or m == 11:
    print('Месяц зимний')
else:
    print('Данный номер не может быть номером месяца')


