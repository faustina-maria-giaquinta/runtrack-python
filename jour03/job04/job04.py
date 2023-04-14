def fizzbuzz():
    """
    Fonction qui itère les nombres entiers de 1 à 100. Pour les multiples de
    trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
    les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".
    """

    for n in range(0, 101):
        prompt = ''
        if n % 3 == 0:
            prompt += "Fizz"
            
        if n % 5 == 0:
            prompt += "Buzz"
        
        print(prompt or n)

if __name__ == '__main__':
    print(fizzbuzz())