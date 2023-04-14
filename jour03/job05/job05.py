# Fonction pour déterminer si un nombre est premier
def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True


if __name__ == "__main__":
    for nombre in range(2, 1000 + 1):
        if est_premier(nombre):
            print(nombre)