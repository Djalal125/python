while True:
    a = float(input("ENTREZ LE PREMIER NOMBRE : "))

    cal = input("Entrez l'opérateur souhaité (+, -, *, /) : ")

    b = float(input("ENTREZ LE DEUXIÈME NOMBRE : "))

    resultat = None
    if cal == "+":
        resultat = a + b
    elif cal == "-":
        resultat = a - b
    elif cal == "*":
        resultat = a * b
    elif cal == "/":
        if b != 0:
            resultat = a / b
        else:
            resultat = "ERREUR : division par zéro"
    else:
        print("Opérateur inexistant")
        continue  # on recommence la boucle

    print("Résultat :", resultat)

    choix = input("Voulez-vous faire d'autre calcul ? (oui/non) : ").lower()
    if choix != "oui":
        print("Merci d'avoir utilisé la calculatrice !")
        break
