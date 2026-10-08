summ = 7384
hour = summ // 3600
min = (summ % 3600) // 60
sec = summ % 60
print(f'{hour:02d}:{min:02d}:{sec:02d}')
