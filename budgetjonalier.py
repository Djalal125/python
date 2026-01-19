def calculateur_budget_journalier():
    
    depenses = []
    # Dictionnaire pour le bonus (catégorie la plus coûteuse)
    depenses_par_categorie = {}
    
    print("CALCULATEUR DE BUDGET JOURNALIER de")
    print("Entrez vos dépenses (ex: 15.50 nourriture). Tapez 'stop' pour terminer.")

    while True:
        entree = input("\nEntrez une dépense et sa catégorie (ex: 20 transport) ou 'stop' : ").strip().lower()

        if entree == 'stop':
            break

        try:
            # Séparer le montant et la catégorie
            parties = entree.split(maxsplit=1)
            if len(parties) < 2:
                print("Format invalide. Utilisez 'montant catégorie' (ex: 20 transport).")
                continue
                
            montant = float(parties[0].replace(',', '.'))
            categorie = parties[1].capitalize()

            if montant <= 0:
                print("Le montant doit être positif.")
                continue

            # Ajouter à la liste principale
            depenses.append(montant)

            # Mettre à jour le dictionnaire des catégories (Bonus)
            if categorie in depenses_par_categorie:
                depenses_par_categorie[categorie] += montant
            else:
                depenses_par_categorie[categorie] = montant

        except ValueError:
            print("Erreur : Veuillez entrer un montant numérique valide.")
            continue

    # Affichage des résultats finaux si des dépenses ont été enregistrées
    if depenses:
        total_depenses = sum(depenses)
        nombre_depenses = len(depenses)
        moyenne_depenses = total_depenses / nombre_depenses

        print("\n#### **Résumé des dépenses :**")
        print(f"Total des dépenses : **{total_depenses:,.2f}**")
        print(f"Dépense moyenne : **{moyenne_depenses:,.2f}**")

        # Bonus : Catégorie la plus coûteuse
        if depenses_par_categorie:
            categorie_max = max(depenses_par_categorie, key=depenses_par_categorie.get)
            montant_max = depenses_par_categorie[categorie_max]
            print(f"Catégorie la plus coûteuse : **{categorie_max}** ({montant_max:,.2f})")

    else:
        print("\n**Aucune dépense enregistrée** pour la journée.")

# Exécuter le programme
if __name__ == "__main__":
    calculateur_budget_journalier()
