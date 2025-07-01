# дз
# Фраза: ну я типо вообще не понимаю этот язык
# from pyexpat.errors import messages
#
# stop_words = {'ну','типо','короче'}
# text = ''
# lst = ''
# while (messages := input ('Введите сообщение: ')) != '':
#     lst = massage.split()
# for item in lst:
#     if item in stop_words:
#         item = ''
#     else:
#         text
#         print()
# res = sorted(res.split())
# for a,b in enumerate (res,1):
#     print(f'{a}.{b}') # не работает у меня у других работает
# stop_words = {'ну','типо','короче'}
# temp = []
#
# while (massage := input ('Введите сообщение: ')) != '':
#     lst = massage.split()
# for item in lst:
#     if item in stop_words:
#         temp.append(item)
#
# res = sorted(temp.split()) # не работает у меня
# for a,b in enumerate (res, 1):
#     print(f'{a}.{b}')
# # #

# stop_words = {'ну','типо','короче'}
# massage = input('Введите сообщение: ')
# lst= massage.split() # все слова
# res = sorted(set(lst) - stop_words)
# for a,b in enumerate (res, 1):
#     print(f'{a}.{b}') # работает


#  чтобы исключить знаки припинания используем код (revert commite)- откатиться назад
# commas = (',', '!', '.','-','?')
#
# stop_words = {'ну','типо','короче'}
# massage = input('Введите сообщение: ')
# for z in commas:
#     massage = massage.replace(z, '')  # все слова
# lst= massage.split() # все слова
# res = sorted(set(lst) - stop_words)
# for a,b in enumerate (res, 1):
#     print(f'{a}.{b}')# работает

#-----------------------------------
# Списочные выражения (list comprehension)
#-----------------------------------
# 1- вариант
# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(*squares, sep =', ')
# 2 - вариант список квадратов чисел
# squares = [i**2 for i in range(10)] # так эффективнее это списки
#
# print(*squares, sep =', ')
#  список квадратов четных чисел
#squares = [i**2 for i in range(10) if i % 2 == 0] # так эффективнее это списки
#          что ->     закон  ->        условия сначала отрабатывает второй блок потом третий потом первый
#print(*squares, sep =', ')
# произведение i и j
# print([i*j for i in range(3) for j in range(3)])
#
# for i in range(3):
#     for j in range(3):
#         print(i* j)# расписано то что шло вложенным циклом выше
# n = '500 600 700 800'
# print([int(i)for i in n.split()])
# n = '100 200 300 400 500 600 700 800 900'
# approved = [500,800]
# a = [int(i) for i in n.split() if int(i) in approved] # проверять списки чтобы они входили одинаковом формате
# print(a)
#############################################
# Нужно чтобы каждое третье слово попало в список
# text = 'Списочные выражения применяются для эффективности кода'
# res =[a for a in text.split() if (text.index(a)+1)%3 ==0]# не совсем правильно
# print(res)
#print([text[i] for i in range(2,len(text),3)]) # не работает правильно
#print([a for a in text.split()[2::3]])
# операции со списком
