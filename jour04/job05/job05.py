def reemplace_par_somme(L):
    """
    Purpose: 
    """

    idx_somme = [2, 4]
    L[3] = sum([L[ent] for ent in idx_somme])

    return f"La valeur de L[-1] est : {L[-1]}."
    
# end def


if __name__ == "__main__":
    import random as rd
    L = [rd.randint(1, 30) for ent in range(5)]
    print(f"La liste créé est : {L}.")
    print(L[1])

    print(reemplace_par_somme(L))
# end main