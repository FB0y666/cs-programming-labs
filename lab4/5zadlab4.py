a = int(input('Номер года: '))
if a<0 or a>9999:
    print('Ошибка')
elif a%400==0 or (a%4==0 and a%100!=0):
    print('Високосный')
else:
    print("Невисокосный")

