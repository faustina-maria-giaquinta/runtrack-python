def possible_construir_triangle(a, b, c):
    """
    La function prend 3 paramètres comme longuers :
    Cela determine si est possible construir un triangle et quel type.
    """
    types_triangles = ['équilatéral',
                        'rectangle',  
                        'isocèle', 
                        'quelconque']
    
    sides = Counter([a, b, c])
    n_equal_sides = len(sides.most_common())
    
    if n_equal_sides == 1:
        return types_triangles[0]
    elif n_equal_sides == 2:
        x = sides.most_common()
        y = [H for H in sides if H != x][0]
        print(y > x and y**2 == 2*(x**2))
        if y > x and y**2 == 2*(x**2):
            return types_triangles[1]
        else:
            return types_triangles[2]
    else:
        return types_triangles[3]





if __name__ == '__main__':
    from collections import Counter
    from math import sqrt

    types = {
        'rectangle': [1, 1, sqrt(2)], 
        # 'isocèle': [6, 6, 4], 
        # 'équilatéral': [5, 5, 5], 
        # 'quelconque': [6, 20, 8]
    }

    
    for test, values in types.items():
        # values = types[test].keys()
        print(values)
        print(possible_construir_triangle(*values))