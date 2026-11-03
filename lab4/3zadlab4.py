x = int(input('Ведите значение для x:'))
y = int(input('Ведите значение для y:'))
if x==0 and  y==0:
    print('Начало координат')
elif x>0 and y==0:
    print('Ось X')
elif x==0 and y>0:
    print('Ось Y')
elif x>0 and y>0:
    print('I четверть')
elif x<0 and y>0:
    print('II четверть')
elif x<0 and y<0:
    print('III четверть')
else:
    print('IV четверть')