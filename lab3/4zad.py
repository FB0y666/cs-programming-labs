a = input()
num, fro, to, time, cost = a.split(';')
print('Поезд:', num)
print('Маршрут:', f'{fro} - {to}')         # f'{}' Они позволяют вставлять значения переменных прямо внутрь строки
print('Отправлеие:', time)
print('Цена:', f'{float(cost):.2f} руб')

