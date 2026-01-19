import sys
import random # Importation du module random (Notions nécessaires)

def tirage_au_sort_gagnant():
    """
    Demande une liste de noms aux utilisateurs et choisit un gagnant au hasard.
    """
    participants = []
    
    print("Bienvenue dans l'outil de tirage au sort de gagnant.")
    print("Entrez les noms des participants un par un.")
    print("Tapez 'fin' lorsque vous avez ajouté tous les participants.")

    # Boucle pour saisir les noms (Notions nécessaires)
    while True:
        nom = input(f"Ajouter un participant (Total: {len(participants)}) ou 'fin' : ").strip().capitalize()
        
        if nom.lower() == 'fin':
            if len(participants) < 2:
                print("Il faut au moins 2 participants pour un tirage au sort.")
                continue
            else:
                break
        
        if nom and nom not in participants:
            # Ajouter dans une liste (Notions nécessaires)
            participants.append(nom)
            print(f"'{nom}' ajouté.")
        elif nom in participants:
            print(f"'{nom}' est déjà dans la liste.")

    # Afficher la liste des participants
    print(f"\n#### **Participants enregistrés ({len(participants)}) :**")
    print(", ".join(participants))

    # Choix aléatoire (Notions nécessaires)
    # random.choice() permet de sélectionner un élément au hasard dans une liste
    gagnant = random.choice(participants)

    # Afficher le gagnant
    print("\n#### **Résultat du tirage au sort :**")
    print(f"Le grand gagnant est : **{gagnant}** !")

# Exécuter le programme
if __name__ == "__main__":
    tirage_au_sort_gagnant()
