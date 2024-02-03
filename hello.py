v = True
while v == True :
    a = int(input('Donnez-moi un nombre : '))
    print(a)

    for i in range(1, 11):
        resultat = a * i
        print(str(a) + " x " + str(i) + ' = ' + str(resultat))
        
    k = input("est ce que vous souhaitez terminer le programme (oui/non) : ")
    if k.lower() == "non":
        v = False
    else : 
        v = "True"
        
print("Fin du programme")
        
