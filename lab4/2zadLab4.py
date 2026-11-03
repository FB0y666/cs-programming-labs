price = int(input("Стоимость:"))
age = int(input('Возраст:'))
if price <= 0 or age < 0 or age > 120:
    print("Ошибка")
else:
    if age <= 5:
        k = 0
    elif age <= 17:
        k = 0.5
    elif age <= 59:
        k = 1
    else:
        k = 0.7
print(f"Стоимость: {price * k:.2f} руб")