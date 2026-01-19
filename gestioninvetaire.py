import sys

def gestion_inventaire_simple():
    """
    Gérer un inventaire simple de produits en mémoire.
    Les produits sont stockés dans une liste de dictionnaires.
    """
    # L'inventaire est une liste de dictionnaires : 
    
    inventaire = []
    
    print("Systeme de gestion d'inventaire SUPER SIMPLE.")

    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un produit")
        print("2. Afficher l'inventaire")
        print("3. Supprimer un produit")
        print("4. Quitter")
        
        choix = input("Choisissez une option (1-4) : ").strip()

        if choix == '4':
            print("Merci et à la prochaine.Fermeture du programme.")
            break
        elif choix == '1':
            # Ajouter un produit
            nom = input("Entrez le nom du produit : ").strip().capitalize()
            try:
                quantite = int(input(f"Entrez la quantité de '{nom}' : ").strip())
                prix = float(input(f"Entrez le prix unitaire de '{nom}' : ").strip().replace(',', '.'))
                if quantite <= 0 or prix <= 0:
                    print("La quantité et le prix doivent être positifs.")
                    continue
                    
                # Vérifier si le produit existe déjà pour mettre à jour la quantité
                trouve = False
                for produit in inventaire:
                    if produit['nom'] == nom:
                        produit['quantite'] += quantite
                        trouve = True
                        break
                
                if not trouve:
                    inventaire.append({"nom": nom, "quantite": quantite, "prix": prix})
                    
                print(f"Produit '{nom}' ajouté/mis à jour.")
            except ValueError:
                print("Erreur : Veuillez entrer des nombres valides pour la quantité et le prix.")
        
        elif choix == '2':
            # Afficher l'inventaire 
            if not inventaire:
                print("L'inventaire est vide.")
            else:
                print("\n#### **État de l'inventaire :**")
                valeur_totale = 0 
                for i, produit in enumerate(inventaire):
                    valeur_produit = produit['quantite'] * produit['prix']
                    valeur_totale += valeur_produit
                    print(f"{i+1}. {produit['nom']} | Qté: {produit['quantite']} | Prix U: {produit['prix']:,.2f} | Valeur: {valeur_produit:,.2f}")
                
                print(f"\n#### **Valeur totale de l'inventaire : {valeur_totale:,.2f}**")
        
        elif choix == '3':
            # Supprimer un produit
            nom_a_supprimer = input("Entrez le nom du produit à supprimer : ").strip().capitalize()
            produit_supprime = False
            for i, produit in enumerate(inventaire):
                if produit['nom'] == nom_a_supprimer:
                    del inventaire[i] # Utilisation de del pour supprimer par index
                    produit_supprime = True
                    break
            
            if produit_supprime:
                print(f"Produit '{nom_a_supprimer}' supprimé.")
            else:
                print(f"Produit '{nom_a_supprimer}' non trouvé dans l'inventaire.")

        else:
            print("Option invalide. Veuillez choisir un numéro entre 1 et 4.")

# Exécution  du  programme
if __name__ == "__main__":
    gestion_inventaire_simple()
