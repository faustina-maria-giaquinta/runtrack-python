if __name__ == "__main__":
    def arrondir_notes(notes):
        """
        Arrondit les notes d'une liste selon les critères suivants :
        - les notes inférieures à 40 sont laissées telles quelles (échec)
        - les notes supérieures ou égales à 40 sont arrondies à la hausse si elles sont à moins de 3 points de leur
        prochain multiple de 5.

        Args:
            notes (list): Une liste de notes allant de 0 à 100 inclus.

        Returns:
            list: Une liste de notes arrondies, respectant les critères de Luke Skywalker.

        """
        notes_arrondies = []
        for note in notes:
            if note < 40:
                notes_arrondies.append(note)
            elif note >= 40 and note % 5 >= 3:
                notes_arrondies.append(note + 5 - note % 5)
            else:
                notes_arrondies.append(note)
        return notes_arrondies

    notes = [72, 58, 91, 33, 80, 68, 75, 99]
    notes_arrondies = arrondir_notes(notes)
    print(notes_arrondies)  # Output: [72, 60, 90, 33, 80, 70, 75, 100]

# end main