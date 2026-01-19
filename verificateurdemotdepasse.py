import string

def verificateur_mot_de_passe():
    
    print("VERIFICATION DE MOT DE PASSE ")

    while True:
        mot_de_passe = input("Entrez un mot de passe à évaluer (ou 'quitter') : ").strip()

        if mot_de_passe.lower() == 'quitter':
            print("Au revoir et merci pour votre fidélité!")
            break

        if not mot_de_passe:
            print("Veuillez entrer un mot de passe:")
            continue

        
        longueur_valide = len(mot_de_passe) >= 8
        contient_chiffre = False
        contient_majuscule = False
        contient_symbole = False # Bonus
        
        
        symboles = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        
        
        for char in mot_de_passe:
            if char.isnumeric():
                contient_chiffre = True
            if char.isupper():
                contient_majuscule = True
            if char in symboles:
                contient_symbole = True

        
        force = ""
        conseils = []

        if longueur_valide and contient_chiffre and contient_majuscule and contient_symbole:
            force = "Fort"
            conseils.append("Excellent ! Votre mot de passe est très sécurisé.")
        elif longueur_valide and contient_chiffre and contient_majuscule:
            force = "Moyen"
            conseils.append("Bon mot de passe. Pour le rendre fort, ajoutez des symboles spéciaux.")
        else:
            force = "Faible"
            if not longueur_valide:
                conseils.append("Le mot de passe doit contenir au moins 8 caractères.")
            if not contient_chiffre:
                conseils.append("Le mot de passe doit contenir au moins un chiffre.")
            if not contient_majuscule:
                conseils.append("Le mot de passe doit contenir au moins une majuscule.")
            if not contient_symbole:
                conseils.append("Pensez à ajouter des symboles spéciaux (!, @, #, etc.).")

        
        print(f"\n#### **Évaluation :**")
        print(f"Force du mot de passe : **{force}**")
        print("#### **Conseils personnalisés :**")
        for conseil in conseils:
            print(f"- {conseil}")

# Exécuter le programme
if __name__ == "__main__":
    verificateur_mot_de_passe()
