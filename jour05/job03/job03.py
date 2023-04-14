if __name__ == "__main__":
    def tapis(n):
        """
        """
        extreme = f"+{'-' * n}+"
        d_idx = 1
        print(extreme)
        for _ in range(n):
            ligne_mod = ['#'] * n
            ligne_mod[n - d_idx] = ' '
            ligne_mod = ''.join(ligne_mod)
            print(f"|{ligne_mod}|")
            d_idx += 1
        print(extreme)
    # end def

    tapis(10)
# end main