import sys

def convertisseur_de_temps():
    """
    Il faut Convertir des minutes en heures/minutes et vice-versa.
    """
    print("Bienvenue dans le convertisseur de temps.")
    
    while True:
        print("\n--- Menu ---")
        print("1. Minutes vers Heures/Minutes")
        print("2. Heures/Minutes vers Minutes")
        print("3. Quitter")
        
        choix = input("Choisissez une option (1-3) : ").strip()

        if choix == '3':
            print("Merci et  aurevoir. Fermeture du programme.")
            break
        elif choix == '1':
            try:
                minutes_input = int(input("Entrez le nombre de minutes à convertir : ").strip())
                if minutes_input < 0:
                    print("Veuillez entrer un nombre positif svp.")
                    continue

                # Notions nécessaires : Division entière et Modulo
                heures = minutes_input // 60
                minutes_restantes = minutes_input % 60
                
                print(f"#### **Résultat :**")
                print(f"{minutes_input} minutes = **{heures}h {minutes_restantes}min**.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier valide svp.")
        
        elif choix == '2':
            #  Faire l'inverse (HH:MM → minutes)
            try:
                heures_input = int(input("Entrez le nombre d'heures : ").strip())
                minutes_input = int(input("Entrez le nombre de minutes : ").strip())
                
                if heures_input < 0 or minutes_input < 0:
                     print("Veuillez entrer des nombres positifs.")
                     continue
                     
                minutes_totales = (heures_input * 60) + minutes_input
                
                print(f"#### **Résultat :**")
                print(f"{heures_input}h {minutes_input}min = **{minutes_totales} minutes**.")

            except ValueError:
                print("Erreur : Veuillez entrer des nombres entiers valides.")
        
        else:
            print("Option introuvable. Veuillez choisir un numéro entre 1 et 3 svp.")

# Exécuter le programme
if __name__ == "__main__":
    convertisseur_de_temps()
