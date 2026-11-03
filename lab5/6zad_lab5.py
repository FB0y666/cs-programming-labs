n = int(input())
row = [1]
odd_count = 0
for i in range(n):
    print(" ".join(str(x) for x in row))
    for x in row:
        if x % 2 != 0:
            odd_count += 1
    new_row = [1]
    for j in range(len(row) - 1):
        new_row.append(row[j] + row[j + 1])
    new_row.append(1)
    row = new_row
print("Нечетных элементов:", odd_count)


