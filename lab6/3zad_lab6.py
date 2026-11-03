n = int(input())
if n < 2:
    print("Ошибка")
else:
    x = []
    d = 2
    while n > 1:
        while n % d == 0:
            x.append(d)
            n //= d
        d += 1
    print(" ".join(map(str, x)))


