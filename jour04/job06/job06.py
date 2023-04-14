def echange_vals(L):
    """
    La fonctione échange les valeurs de la première et de la dernière case d’une
    liste quelconque non vide.
    """
    if not len(L):
        return "La liste est vide."

    else:
        idx_changer = [0, -1]
        valeurs = [L[idx] for idx in idx_changer]
        for idx in idx_changer:
            L[idx] = valeurs[::-1][idx]
    
    return L
    
# end def


if __name__ == "__main__":
    import random as rd
    L = [rd.randint(1, 30) for ent in range(5)]
    print(f"La liste créé est : {L}.")

    print(echange_vals(L))
# end main