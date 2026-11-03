n = int(input())
if n<0:
    print('Ошибка')
else:
    count = 0
    total = 0
    if n == 0:
        count = 1
        total = 0
    else:
        while n > 0:
            a = n % 10
            total += a
            count += 1
            n //= 10
    print("Цифр:", count)
    print("Сумма цифр:", total)

