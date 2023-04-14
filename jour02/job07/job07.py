def positif_ou_negatif(nombre):
    """
    La function prend en paramètre un nombre est :
    - afiche "positif" si le nombre est supérior à 0
    - afiche "negatif" si le nombre est inférieur à 0.
    """

    return "positif" if nombre > 0 else "negatif"

if __name__ == '__main__':
    import random
    
    for nombre in random.sample(range(-15,28), 5) :
        print(f"{nombre} est {positif_ou_negatif(nombre)}")