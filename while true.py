
while True:
    a = input('Введите целое число a: ')
    b = input('Введите целое число b: ')
##    if a.isdigit() and b.isdigit() \
##    or (a [0]== '-' and a[1:].isdigit() and (b [0]== '-' and b[1:].isdigit()):
##        a = int(a)
##        b = int(b)
##        break
##    print('Вводите целые числа')
    if a.isdigit() or a[0] == '-' and a[1:].isdigit():
        a = int(a)
    if b.isdigit() or b[0] == '-' and b[1:].isdigit():
        b = int(b)
    if type(a) == type(b) == int:
        break
    print('Нужно вводить целые числа')
s = 0
if a > b:
    a, b = b, a
for i in range(a + 1, b):
    s += i **2
print(s)
