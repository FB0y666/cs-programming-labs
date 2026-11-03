a = int(input())
b = int(input())
if a<0 or b<0 or (a<0 and b<0):
    print("Ошибка")
else:
    x,y=a,b
    while y!=0:
        x,y= y, x % y
    print("НОД:", x)



