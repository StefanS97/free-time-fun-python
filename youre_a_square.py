import math

def is_square(n):
    try:
        square = math.sqrt(n)

        if int(square + 0.5) ** 2 == n:
            return True
        else:
            return False
    except ValueError:
            return False