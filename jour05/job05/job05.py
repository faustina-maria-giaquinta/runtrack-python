if __name__ == "__main__":
    def marches(x, y):
        """
        Calcule la distance parcourue par un gardien de phare pour aller aux toilettes en fonction
        du nombre de marches et de la hauteur de chaque marche.

        Args:
            x (int): Le nombre de marches du phare.
            y (int): La hauteur de chaque marche en centimètres.

        Returns:
            str: Une chaîne de caractères au format 'Pour x marches de y cm, le gardien parcours z.zz m par semaine.'
                où x est le nombre de marches, y est la hauteur de chaque marche et z.zz est la distance parcourue
                en mètres arrondie à deux décimales.

        Note:
            Le gardien de phare va aux toilettes cinq fois par jour, les toilettes sont au rez-de-chaussée et il
            doit remonter après être descendu.
        """

        distance_jour = (x * y * 2) * 0.01
        distance_semaine = distance_jour * 5 * 7

        return f"Pour {x} marches de {y} cm, le gardien parcours {distance_semaine:.2f} m par semaine"
    # end def
# end main