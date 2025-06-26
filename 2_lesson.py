"""word = str(input('введите слово из трёх символов: '))
if len(word) <= 3:
    print('слово подходит')
else:
    print('Введите слово заново')

while len(word) <= 3:
    word = input('введите слово из трёх символов: ')

print(f'В ввели слово: {word}')

while len(word := input('введите слово из трёх символов: ')) <= 3:
    print(f'слово: "{word}" слишком короткое.')

print(f'В ввели слово: {word}')
# := -оператор морж  двоеточие и равно  присваевает переменную чтобы сократить код

# без использования моржа
word = str(input('введите слово: '))
while word != '':
    print(f'слово: "{word}"')
    word = input('введите слово: ')
print(f'Пустая строка введена')


# с использованием операции морж
while (word := input('введите слово: ')) != '':
    print(f'слово: "{word}"')

print(f'Пустая строка введена')

 Flag э то переменная которая переключается с true на folse

num = 3 #  число , которое надо угодать
flag = True # флаг изменяет значение по событию. можно писать вместо true 1. это flag = 1
print('Я загодал число, угодай!')
while flag:  # здесь вместо флага можно поставить true и тогда это будет вечный цикл.
    var = input(input('Ваше значение: '))
    if var == num:
        print('Ура. угодал')
        break
        flag = not flag # флаг инвертирован
        # аналогично flag = false
    elif var >num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')
print('Приходи ещё!')
# break -перерыв программа вылетает
# continue

counter = 0
# цикл из 5 итераций
while counter < 5:
    counter += 1
    if counter == 3:
        continue
        # прервать текущую итерацию и начать следующую. в данном случае он не выведет 3 пропустит ее и продолжает. выведет 1,2,4,5
    print(f'Итерация номер :{counter}' )
# 1 вариант
height = int(input('какой рост: '))
while height >= 150 and height <= 180:
    print('Вы нам не подходите: ')
    break
else:
    print('мы вас берём')
# 2 вариант
height = int(input('какой рост: '))
while height >= 150 and height <= 180:
    print('Вы нам не подходите: ')
    height = int(input('какой рост: '))
else:
    print('мы вас берём')
# 3 вариант
height = int(input('какой рост: '))
while not(150<= height >= 180):
    print('Вы нам не подходите: ')
    height = int(input('какой рост: '))
else:
    print('мы вас берём')

from re import match

# match - case (3.10>)
print('Возможные ходы: \n\tL - влево\n\tR - вправо\n\tF- прямо')
while  True:# туту тогда тоже вместо True будет flag
    ch = input('Ваш выбор:')
match ch:
    case 'L'| 'l'| 'д'| 'Д':
        print('Cвернули налево')
    case 'R'| 'к'| 'r'| 'K':
        print('Cвернули направо')
    case 'F'| 'а'| 'А'| 'f':
        print('Cвернули прямо')
    case 'Q' | 'q' | 'й' | 'Й':
        print('Cвернули прямо')
        break # flag= Folse можно выйти м помощью flag
    case _: #default
        print('выбор не ясен')

# сгенерировать числа от одного до ста, но выводить числа с окончанием 3
counter = 1
while counter <=100:
    if counter % 10 ==3:
       counter +=1

    print(counter) # бесконечный цикл подумай как остановить.

# ключевое слово in
word = 'поток'
if 'ток' in word:

# цикл for
# for <переменная> in iterable:
# команда
word = 'поток'
for ch in word:
    print(ch)
         #   0      3     1
# итератор range(start, stop,step)
for i in range(0,6,1):
    print(i)# последнее число не выводит

for i in range(2,13,2):
    print(i)# выводит четные числа до 12
for i in range(13,2):
    print(i)# выведет от 0 до 12 с шагом 2
for i in range(13):
    print(i)# выводит числа от 0 до 12 с шагом 1

for _ in range(10):
    print('Привет')# выводит слово 9 раз

for i in range(1,101):
    if i %10 == 5:
print( i )# выводит все числа которые заканчиваются на 5

for i in range(1,101):
    if i %10 == 5:
        if i == 15:
            continue
        print( i )# выводит все числа которые заканчиваются на 5
        #ещё один вариант
for i in range(1,101):
    if i %10 == 5 and i != 15:

        print( i )# выводит все числа которые заканчиваются на 5

for i in range(100,1):
    print( i )  # выводит все числа от 100 до 2

for i in reversed(range(100,1)):
    print(i)  # выводит все числа от 100 до 2
"""
for i in reversed(range(5,96,5)):
    print(i)  # выводит все числа от 100 до 2