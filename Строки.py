##print(1, 2, 3, sep='\r')

s1 = 'Привет'
s2 = 'Мир'

print(s1, s2, sep='\r')
print(s1, s2, end='\r')
print(s1, s2, end='\n')
print('черта \'')
print('черта \\ ')
print('Привет, %s' % 'Вася')
print('Привет, %s. Тебе %s' % ('Вася', '20'))
print('Привет, %s. Тебе %s' % ('Вася', 20))
print('Привет, %s. Тебе %d' % ('Вася', 20))
print('Привет, %s. Тебе %i' % ('Вася', 20))
print('Привет, %s. Тебе %f' % ('Вася', 20))
print('Привет, %s. Тебе %f' % ('Вася', 20.2))
print('Привет, %s. Тебе %.f' % ('Вася', 20.2))
print('Привет, %s. Тебе %.1f' % ('Вася', 20.2))
print('Привет, %s. Тебе %.2f' % ('Вася', 20.2))
print('Привет, %s. Тебе %+.2f' % ('Вася', 20.2))
print('Привет, %s. Тебе %+.2f' % ('Вася', -20.2))
print('Привет, %s. Тебе % .2f' % ('Вася', -20.2))
print('Привет, %s. Тебе % .2f' % ('Вася', 7.656586586464646))
print('Привет, %s. Тебе % .2e' % ('Вася', 7.656586586464646))
print('Привет, %s. Тебе % .1e' % ('Вася', 7.656586586464646))
print('Привет, %s. Тебе %g' % ('Вася', 748000000000000))

##x = 12.896866866977
##a = '%.3f' % х
##
##print('меня зовут {1}. Мне {} лет' .format('Вася', 12))
##print('меня зовут {name}. Мне {} лет '.format(name = 'Вася', 12))

print('меня зовут {:.2f}.  Мне {age:.3f} лет'.format(2.564, age = 12))
print(f'меня зовут {2.564:.2f}. Мне {12:.3f} лет')

s = 'hello'
s[0]
print(s[0])
print(s[2:0])


