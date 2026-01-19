import time

def quiz_educatif_simple():
    """
    QUESTIONNAIRE EDUCATIF
    """

    # Liste de dictionnaires de questions et réponses
    questions_data = [
        {
            "question": "Quelle est la capitale de la France ?",
            "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "answer": "c",
            "correction": "Paris est la capitale de la France."
        },
        {
            "question": "En quelle année le Bénin a obtenu son indépendance ?",
            "options": ["a) 1990", "b) 2024", "c) 1960", "d) 1880"],
            "answer": "c",
            "correction": "Le Bénin a obtenu son indépendance en 1960."
        },
        {
            "question": "Quel est le résultat de 5 * 2 ?",
            "options": ["a) 40", "b) 45", "c) 10", "d) 50"],
            "answer": "c",
            "correction": "5 * 2 est égal à 10."
        },
        {
            "question": "Une année compte combien de jours ?",
            "options": ["a) 45", "b) 3288", "c) 365", "d) 360"],
            "answer": "c",
            "correction": "Une année compte 365 jours."
        },
        {
            "question": "En quelle année l'homme a-t-il marché sur la lune pour la première fois ?",
            "options": ["a) 1959", "b) 1969", "c) 1979", "d) 1989"],
            "answer": "b",
            "correction": "Neil Armstrong a marché sur la lune en 1969."
        }
    ]

    score = 0
    total_questions = len(questions_data)

    print("\n--- Bienvenue dans le questionnaire éducatif ! ---")
    print(f"Le questionnaire comporte {total_questions} questions.")

    for index, q_data in enumerate(questions_data, start=1):
        print(f"\n--- Question {index}/{total_questions} ---")
        print(q_data["question"])

        for option in q_data["options"]:
            print(option)

        reponse_utilisateur = input("Votre réponse (a, b, c ou d) : ").lower()

        if reponse_utilisateur == q_data["answer"]:
            print("Bonne réponse !")
            score += 1
        else:
            print("Mauvaise réponse.")

        print(f"Correction : {q_data['correction']}")
        time.sleep(1)

    print("\n--- Résultats du Questionnaire ---")
    print(f"Vous avez obtenu {score} points sur {total_questions}.")

# Exécution du programme
if __name__ == "__main__":
    quiz_educatif_simple()
