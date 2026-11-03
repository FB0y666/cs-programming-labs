count = 0
total = 0
while True:
    s = input()
    if s == "stop":
        break
    total += int(s)
    count += 1
if count == 0:
    print("Нет покупок")
else:
    print("Покупок:", count)
    print("Общая стоимость:", total, "руб")
    print("Средняя стоимость:", f"{total / count:.2f}", "руб")

