a = int(input('Сторона А = '))
b = int(input("Сторона B = "))
c = int(input("Сторона C = "))
if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print("Треугольник не существует")
elif a==b==c:
    print('Равносторонний')
elif a==b or b==c or c==a:
    print('Равнобедренный')
else:
    print('Разносторонний')

