def parcour_nombres_un_sur_deux():
    """
    Fonction qui parcourt les nombres de 0 à 20 et affiche un nombre chaque deux dans le terminal.
    """
    for _ in range(0, 21, 2):
        print(_)

if __name__ == '__main__':
    print(parcour_nombres_un_sur_deux())