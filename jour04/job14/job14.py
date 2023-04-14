if __name__ == "__main__":
    def my_long_word(n, chaine):
        """
        La fonction trouve la liste des mots qui sont plus longs que n à
        partir d'une chaine de caractères.
        """
        
        return f"{' '.join([mot for mot in chaine.split() if len(mot) > n])}"
    # end def

    assert my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"), "peur chemin vers côté obscur peur mène colère colère mène haine haine mène souffrance"
# end main