def ajouter_melon_fruits():
    """
    La fonction retourne une liste nommée “fruits” qui contient les string
    “pomme”, “cerise”, “orange”. À son appel, ella ajoute à la liste “fruits” une
    String “mangue” à l'index 2'.
    """

    fruits = ['pomme', 'cerise', 'orange', 'melon']
    fruits[2] = 'mangue'

    return fruits
    
# end def

if __name__ == "__main__":
    print(ajouter_melon_fruits())
# end main