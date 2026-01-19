import sys

def generateur_de_ticket():
    
    compteur_ticket = 1
    
    print("GESTION DE NUMEROS DE  TICKETS ")
    print("Tapez 'go' pour générer un nouveau ticket, ou 'stop' pour quitter.")

    while True:
        action = input("\nAction requise ('go' ou 'stop') : ").strip().lower() 

        if action == 'stop':
            print("Fermeture de la gestion  de tickets.")
            break
        elif action == 'go':
            
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
