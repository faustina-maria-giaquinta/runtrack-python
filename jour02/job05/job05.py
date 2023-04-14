def calcule(num1, operator, num2):
    """
    La function prend 3 paramètres :
    - le premier, “num1”, est un nombre,
    - le deuxième, "operator", est un caractère (string) contenant le type d’opération
        (+, -, *, /, %),
    - le troisième, “num2”, est un nombre.

    La fonction retourne le résultat de l’opération.
    """

    ops = {
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
        '*': lambda num1, num2: num1 * num2,
        '/': lambda num1, num2: num1 / num2,
        '%': lambda num1, num2: num1 % num2
    }
    
    return ops[operator](num1,num2)

if __name__ == '__main__':
    print(calcule(10, '/', 20))