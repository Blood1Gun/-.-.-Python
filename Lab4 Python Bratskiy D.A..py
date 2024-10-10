str = input("Введите строку -> ")

n = 0
for i in str:
    if i == '.':
        str = str.replace(i, '')
        n += 1
print('Полученная строка: ', str,
      '\nКоличество удаленных символов: ', n)

