n = int(input('Введите цифру от 1 до 10: '))
if n > 10 or n < 0:
    print("Ошибка")
else:
    for i in range(n):
        x = []
        for j in range(n):
            if i >= j:
                d = i - j
            else:
                d = j - i
            x.append(str(d))
        print(" ".join(x))


