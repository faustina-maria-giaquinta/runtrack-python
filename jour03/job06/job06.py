
def pyramid():
    """
    La fonction récupère et affiche autant de caractères que possible de cette chaîne sous forme de
    suite pyramidale.
    """
    chaine = "abcdefghijklmnopqrstuvwxyz" * 10 
    n = 1
    i = 0
    
    while i < len(chaine):
        print(chaine[i:i+n])
        i += n
        n += 1

    
if __name__ == "__main__":
    print(pyramid())
# end main