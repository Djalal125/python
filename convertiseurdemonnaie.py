def afficher_menu():

    print("\n===== MENU  =====")
    print("\nVeuillez choisir l'opération à effectuer selon le menu :")
    print("1. FCFA → EUR")
    print("2. FCFA → USD")
    print("3. EUR → FCFA")
    print("4. EUR → USD")
    print("5. USD → FCFA")
    print("6. USD → EUR")
    print("0. Quitter")

def convertisseur_de_monnaie():
    """
    Convertisseur de monnaie avec menu.
    Monnaies : FCFA, EUR, USD
    """
# Les différents taux des monnaies

    TAUX_DE_CHANGE = {
        1: ("FCFA", "EUR", 0.0015),
        2: ("FCFA", "USD", 0.0018),
        3: ("EUR", "FCFA", 655.96),
        4: ("EUR", "USD", 1.18),
        5: ("USD", "FCFA", 558.17),
        6: ("USD", "EUR", 0.85)
    }

    print("Bienvenue dans le convertisseur de monnaie ")

# oppération pour faire le choix
    while True:
        afficher_menu()

        try:
            choix = int(input("Choisissez une option : "))
        except ValueError:
            print(" Veuillez entrer un numéro valide pour continuer svp!")
            continue

        if choix == 0:
            print("Merci d'avoir utilisé le convertisseur de monnaie. Au revoir ")
            break

        if choix not in TAUX_DE_CHANGE:
            print(" Option invalide. veuillez reprendre svp!")
            continue

        try:
            montant = float(input("Entrez le montant à convertir : "))
        except ValueError:
            print(" Montant invalide.")
            continue

        monnaie_source, monnaie_cible, taux = TAUX_DE_CHANGE[choix]
        montant_converti = montant * taux

        print("\n===== RÉSULTAT =====")
        print(f"{montant:,.2f} {monnaie_source} = {montant_converti:,.2f} {monnaie_cible}")


# Lancement du programme
if __name__ == "__main__":
    convertisseur_de_monnaie()
