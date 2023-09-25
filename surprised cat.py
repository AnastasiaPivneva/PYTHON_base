a1 = "    /\_/\    "
a2 = "   / @ @ \   "
a3 = "  ( > 0 < )  "
a4 = "  '>>>x<<<'  "
a5 = " /    1    \ "

n = int(input('Введите n: '))
for i in range(n):
    print(a1, end=' ')
print()
for i in range(n):
    print(a2, end=' ')
print()
for i in range(n):
    print(a3, end=' ')
print()
for i in range(n):
    print(a4, end=' ')
print()
for i in range(1, n+1):
    print(f" /    {i}    \ ", end=' ')
