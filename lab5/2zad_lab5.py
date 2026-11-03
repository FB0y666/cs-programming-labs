a = int(input())
b = int(input())
count = 0
c = 1
for i in range(a, b + 1):
    count += i
    c *= i
print("Сумма:", count)
print("Произведение:", c)
