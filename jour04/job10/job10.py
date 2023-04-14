if __name__ == "__main__":
    intervalle = [25, 90]
    prod = 1
    for _ in range(*intervalle):
        prod *= _

    print(f"le produit de toutes les valeurs de la liste comprises dans l’intervalle [25, 90], est : {prod}.")
# end main