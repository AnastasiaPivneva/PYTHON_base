##flag = True
##while flag:
##    n = input('Введите число ')
##    if n.isdigit() or (n [0]== '-' and n[1:].isdigit()):
##        n = int(n)
##        flag = False

##while True:
##    n = input('Введите число ')
##    if n.isdigit() or (n [0]== '-' and n[1:].isdigit()):
##        n = int(n)
##        break
flag = True
while flag:
    n = input('Введите число ')
    if n.isdigit() or (n [0]== '-' and n[1:].isdigit()):
        n = int(n)
        flag = False
        if 10 <= n <= 20:
            break
    print('привет')
else:
    print('Цикл сработал')
