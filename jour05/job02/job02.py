if __name__ == "__main__":
    def draw_rectangle(width, height):
        """
        """
        extreme = f"|{'-' * width}|"
        print(extreme)
        for _ in range(height - 2):
            print(f"|{' ' * width}|")
        print(extreme)
    # end def

    draw_rectangle(10, 3)
# end main