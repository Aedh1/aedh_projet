a = int(input('Donnez-moi un nombre : '))
print(a)

for i in range(1, 11):
    resultat = a * i
    print(str(a) + " x " + str(i) + ' = ' + str(resultat))
