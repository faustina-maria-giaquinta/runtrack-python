def nourriture_a_manger(type_, saison):
    """
    La function prend 2 paramètres :
    - Le premier reçoit un String nommé “type”
    - Le second reçoit un String nommé “saison”

    Combinaisons possibles:
    - Si la valeur de “type” est égal à “fruits” et que celle de saison est égal à “hiver”, affichez
    “orange, mandarine et kiwi”
    - Si la valeur de “type” est égal à “fruits” et que celle de saison est égal à “ete”, affichez
    “Poire, fraise, cassis”
    - Si la valeur de “type” est égal à “legume” et que celle de saison est égal à “hiver”,
    affichez “carotte, topinambour, endive”
    - Si la valeur de “type” est égal à “legume” et que celle de saison est égal à “ete”, affichez
    “artichaut, aubergine,navet”
    """

    saisons = {
        'hiver': {'fruits': "orange, mandarine et kiwi",
                  'legume': "carotte, topinambour, endive"},
        'été': {'fruits': "poire, fraise, cassis",
                'legume': "artichaut, aubergine, navet"}
    }

    return saisons[saison][type_]

if __name__ == '__main__':
    import random

    seasons = ['hiver', 'été']
    types = ['fruits', 'legume']
    
    for _ in range(10):
        season = random.choice(seasons)
        type_ = random.choice(types)
        print(f"La saison est {season} donc les {type_} que tu devrais manger sont {nourriture_a_manger(type_, season)}.")