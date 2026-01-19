import sys

def convertisseur_imc():
    """
    Calcule l'Indice de Masse Corporelle (IMC) et détermine la catégorie associée.
    """
    print("Bienvenue dans le convertisseur d'IMC.")

    while True:
        try:
            poids_str = input("Entrez votre poids en kg (ou 'quitter' pour sortir) : ").strip().replace(',', '.')
            if poids_str.lower() == 'quitter':
                print("Fermeture du programme.")
                break
            
            taille_str = input("Entrez votre taille en mètres (ex: 1.75) : ").strip().replace(',', '.')

            poids = float(poids_str)
            taille = float(taille_str)

            if poids <= 0 or taille <= 0:
                print("Le poids et la taille doivent être des valeurs positives.")
                continue

            #  Calculs (IMC = poids / (taille²))
            imc = poids / (taille ** 2)

            categorie = ""
            conseil = ""

            # Notions nécessaires : Conditions
            if imc < 18.5:
                categorie = "Maigreur"
                conseil = "Vous êtes en sous-poids. Pensez à consulter un nutritionniste pour un régime adapté."
            elif 18.5 <= imc < 25:
                categorie = "Normal"
                conseil = "Votre poids est normal. Maintenez une alimentation équilibrée et une activité physique régulière."
            elif 25 <= imc < 30:
                categorie = "Surpoids"
                conseil = "Vous êtes en surpoids. Faire plus d'exercice et surveiller votre alimentation pourrait être bénéfique."
            else:
                categorie = "Obésité"
                conseil = "Vous êtes en situation d'obésité. Il est fortement recommandé de consulter un professionnel de santé."

            # Affichage du résultat et du conseil (Bonus)
            print(f"\n#### **Résultat IMC :**")
            print(f"Votre IMC est de **{imc:,.2f}**.")
            print(f"Catégorie : **{categorie}**.")
            print(f"#### **Conseil :**")
            print(conseil)

        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
        
        # Message d'avertissement
        print("\n*Avertissement : Cet outil est à titre informatif uniquement et ne remplace pas un avis médical professionnel.*")


# Exécuter le programme
if __name__ == "__main__":
    convertisseur_imc()

