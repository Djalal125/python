import sys

def gerer_presences():
    
    
    liste_presences = {}
    
    print("GESTION DE PRESENCE SIMPLE")

    while True:
        print("\n--- Menu ---")
        print("1. Ajouter une présence")
        print("2. Afficher la liste des présents")
        print("3. Exporter la liste dans presence.txt (Bonus)")
        print("4. Quitter")
        
        choix = input("Choisissez une option (1-4) : ").strip()

        if choix == '4':
            print("Fermeture du programme.")
            break
        elif choix == '1':
            nom = input("Entrez le nom de la personne : ").strip().capitalize()
            statut = input(f"La personne '{nom}' est-elle présente ? (oui/non) : ").strip().lower()
            liste_presences[nom] = (statut == 'oui' or statut == 'o')
            print(f"Statut de {nom} enregistré.")
        elif choix == '2':
            if not liste_presences:
                print("La liste de présence est vide.")
            else:
                print("\n#### **Liste des participants :**")
                # Compter le nombre total de présents (Bonus)
                presents = [nom for nom, present in liste_presences.items() if present]
                absents = [nom for nom, present in liste_presences.items() if not present]
                
                print(f"Total des personnes : {len(liste_presences)}")
                print(f"Total des présents : **{len(presents)}**")
                print("Présents :", ", ".join(presents) if presents else "Aucun")
                print("Absents :", ", ".join(absents) if absents else "Aucun")
        elif choix == '3':
            # Exporter dans un fichier presence.txt (Bonus)
            try:
                with open("presence.txt", "w", encoding="utf-8") as f:
                    f.write("--- Rapport de Présence ---\n")
                    f.write(f"Total des participants : {len(liste_presences)}\n")
                    f.write(f"Total des présents : {len([p for p in liste_presences.values() if p])}\n\n")
                    for nom, present in liste_presences.items():
                        statut_texte = "PRÉSENT" if present else "ABSENT"
                        f.write(f"- {nom}: {statut_texte}\n")
                print("Liste exportée avec succès dans le fichier 'presence.txt'.")
            except IOError as e:
                print(f"Erreur lors de l'écriture du fichier : {e}")
        else:
            print("Option invalide. Veuillez choisir un numéro entre 1 et 4.")

# Exécuter le programme
if __name__ == "__main__":
    gerer_presences()
