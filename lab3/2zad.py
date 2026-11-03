a = input()
f,i,o = a.split()
f2,i2,o2 = [x.capitalize() for x in (f,i,o)] #capitalize делает первую букву заглавной
print(f2,i2[0]+'.',o2[0]+'.')



