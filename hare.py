s1 = "    /)/)    "
s2 = "  =('.')=   "
s3 = "~~( #1# )~~ "
##print(len(s3))
##print(s1)
##print(s2)
##print(s3)
n = int(input('Введите n: '))
for i in range(n):
    print(s1, end=' ')
print()
for i in range(n):
    print(s2, end=' ')
print()
for i in range(1, n+1):
    print(f"~~( #{i}# )~~ ", end=' ')
