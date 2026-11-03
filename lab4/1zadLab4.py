a = input('Текушая температура:')
b = input('Желаемая температура:')
if a>b:
    print('Охлаждение')
elif b<a:
    print('Нагрев')
elif a==b:
    print('Выключен')


