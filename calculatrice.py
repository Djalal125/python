
a = float(input("ENTREZ LE PREMIER NOMBRE : "))

cal = input("Entrez l'operateur souhaiter (+, -, *, /) :")

b = float(input("ENTREZ LE DEUXIEME NOMBRE : "))

#resultat = float()
if cal == "+" :
    resultat =  a + b 
elif cal == "-" :
    resultat =  a - b 
elif cal == "*" :
    resultat =  a * b
elif cal == "/" :
    if b != 0 :
        resultat =  a / b
    else :
        resultat = "ERREUR"
else :
    print("operateur inexistant")
    
print("resultat :  " , resultat)

