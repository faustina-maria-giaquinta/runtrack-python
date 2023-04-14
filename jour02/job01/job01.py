def my_print_name(name=None):
    """
    Afficher "Hello world" dans la terminal à son appel.
    """
    
    print(name)

if __name__ == "__main__":
    for name in ['Faustina', 'Ade', 'Valente']:
        my_print_name(name)