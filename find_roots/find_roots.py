def find_roots(a, b, c):
    import math
    x=()
    x += (((b * -1) - math.sqrt((b**2) - 4 * a* c))/(2*a), )
    x += (((b * -1) + math.sqrt((b**2) - 4 * a* c))/(2*a),)
    return x

print(find_roots(2, 10, 8))