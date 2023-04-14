def ajouter_melon_fruits():
    """
    La fonction retourne une liste nommée “fruits” qui contient les string
    “pomme”, “cerise”, “orange”. À son appel, ella ajoute à la liste “fruits” une
    String “Melon” à la fin de cette liste.
    """

    fruits = ['pomme', 'cerise', 'orange']
    fruits.append('melon')

    return fruits
    
# end def

if __name__ == "__main__":
    print(ajouter_melon_fruits())
# end main