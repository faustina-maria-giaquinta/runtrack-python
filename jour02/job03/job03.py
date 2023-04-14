def add(num1 = 0, num2 = 0):
    """
    La function prendre 2 nombres entiers en paramètres et affiche la somme de ces entiers.
    """
    
    print(num1 + num2)

if __name__ == '__main__':
    for n1, n2 in [(1, 2), (5, 8), (10,10)]:
        add(n1, n2)