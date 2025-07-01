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
#     print(f'{a}.{b}')

# stop_words = ['ну','типо','короче']
# temp = []
#
# while (messages := input ('Введите сообщение: ')) != '':
#     lst = massage.split()
# for item in lst:
#     if item in stop_words:
#         temp.append(item)
#
# res = sorted(res.split())
# for a,b in enumerate (res, 1):
#     print(f'{a}.{b}')
#

stop_words = {'ну','типо','короче'}
massage = input('Введите сообщение: ')
lst= massage.split() # все слова
res = sorted(set(lst) - stop_words)
for a,b in enumerate (res, 1):
    print(f'{a}.{b}')