name = input('Введите Ваше имя ')
father_name = input('Введите Ваше отчество ')
surname = input('Введите Вашу фамилию ')

name = name[0].upper() + name[1:].lower()
father_name = father_name[0].upper() + father_name[1:].lower()
surname = surname.title()
print(name, father_name, surname)
print(f'Подпись для отзывов: {name} {surname[0]}.')
print('Обращение в письмах: Уважаемый,%s %s!' % (name, father_name))
print('Идентификатор в базе покупателей: {} {}. {}.'.format(surname, name[0], father_name[0]))
