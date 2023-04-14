def parcour_nombres_sauf():
    """
    Fonction qui parcourt les nombres de 0 à 100 et affiche tous les chiffres
    dans le terminal, sauf 26, 37, 88.
    """
    for _ in range(0, 101):
        if _ in [26, 37, 88]:
            pass
        else:
            print(_)

if __name__ == '__main__':
    print(parcour_nombres_sauf())