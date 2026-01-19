import sys

def generateur_de_ticket():
    """
    Génère des numéros de ticket croissants jusqu'à ce que l'utilisateur tape 'stop'.
    """
    compteur_ticket = 1
    
    print("Générateur de numéros de ticket (file d'attente).")
    print("Tapez 'go' pour générer un nouveau ticket, ou 'stop' pour quitter.")

    while True:
        action = input("\nAction ('go' ou 'stop') : ").strip().lower()

        if action == 'stop':
            print("Fermeture du générateur de tickets.")
            break
        elif action == 'go':
            # Formatage de texte pour s'assurer que le numéro fait 3 chiffres (ex: 001)
            numero_formatte = f"{compteur_ticket:03}"
            print(f"#### **Ticket généré :**")
            print(f"Ticket **{numero_formatte}**")
            
            # Incrémenter le compteur (i = i + 1)
            compteur_ticket += 1
        else:
            print("Commande invalide. Veuillez taper 'go' ou 'stop'.")

# Exécuter le programme
if __name__ == "__main__":
    generateur_de_ticket()
