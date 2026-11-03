n = int(input())
if n < 2:
    print("Не простое")
else:
    b = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            b = False
            break
        d += 1
    if b:
        print("Простое")
    else:
        print("Не простое")

