dist = 250
ras = 7.5
prise = 60
fuel_needed = (dist * ras)/100
total_cost =  fuel_needed * prise
print(f'Топливо: {fuel_needed:.2f} л.')
print(f'Стоимость: {total_cost:.2f} руб.')В