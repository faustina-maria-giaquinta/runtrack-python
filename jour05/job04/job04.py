if __name__ == "__main__":
    def cesar(message, decale):
        """
        """
        from string import ascii_lowercase
        import unicodedata

        m_sans_accents = ''.join(c for c in unicodedata.normalize('NFD', message) if unicodedata.category(c) != 'Mn')
        alph = ascii_lowercase

        m_chiffre = ''

        for l in m_sans_accents.lower():
            if l.isalpha():
                if alph.index(l) >= len(alph):
                    m_chiffre += alph[len(alph) - alph.index(l) + decale]
                else:
                    m_chiffre += alph[alph.index(l) + decale]
            else:
                m_chiffre += l
        
        return m_chiffre
        
    # end def

    m = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
    print(cesar(m, 3))
# end main