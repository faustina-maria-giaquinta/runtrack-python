def language_prediction(language = None):
    """
    La function prend en paramètre une String et affiche
    si la valeur de "langage" est égal à:
     - "javascript" -> "tu es un developpeur web",
     - "python" -> "tu es un developpeur IA",
     - "java" -> "tu es un developpeur logiciel",
     - "reactjs" -> "tu es un developpeur mobile".
    Sinon, affichez "un jour, je serai le meilleur developpeur... "
    """

    lang_prompts = {
        "javascript": "tu es un developpeur web",
        "python": "tu es un developpeur IA",
        "java": "tu es un developpeur logiciel",
        "reactjs": "tu es un developpeur mobile"
    }

    return lang_prompts[language] if language in lang_prompts.keys() else "un jour, je serai le meilleur developpeur..."

if __name__ == '__main__':
    import random
    languages = ["javascript", "python", "java", "reactjs"]
    
    for _ in range(10):
        lang = random.choice(languages)
        print(f"If your languages is {lang}, {language_prediction(lang)} !")