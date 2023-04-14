if __name__ == "__main__":
    def modify_word(word):
        """
        Cette fonction prend en entrée une chaîne de caractères composée d'un seul mot, ne contenant que les 26 lettres de l'alphabet en minuscule et sans accents. La fonction modifie le mot en permutant certains ou tous ses caractères afin de créer un nouveau mot qui soit le plus proche possible du mot original dans l'ordre alphabétique. La fonction renvoie le nouveau mot sous forme de chaîne de caractères.
        """
        chars = word.split()

        # Trouver la première paire de caractères tels que le caractère de gauche est inférieur au caractère de droite
        left_char = len(chars) - 2
        while left_char >= 0 and chars[left_char] >= chars[left_char + 1]:
            left_char -= 1

        # Si on ne trouve pas une telle paire, le mot est déjà le plus grand possible, donc on ne modifie pas le mot
        if left_char == -1:
            return word

        # À partir du caractère de droite de cette paire, trouver le plus petit caractère qui soit plus grand que le caractère de gauche de la paire
        right_char = len(chars) - 1
        while chars[right_char] <= chars[left_char]:
            right_char -= 1

        # Échanger les deux caractères
        chars[left_char], chars[right_char] = chars[right_char], chars[left_char]

        # Trier les caractères à droite de la paire dans l'ordre croissant et les ajouter au mot
        chars[left_char + 1:] = sorted(chars[left_char + 1:])

        # Convertir la liste de caractères en un mot et le retourner
        return ''.join(chars)

    word = input("Entrez un mot : ")
    modified_word = modify_word(word)
    print("Le mot modifié est :", modified_word)
# end main