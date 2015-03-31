import math
triangles = [[10, 5, 7], [10, 5, 6], [10, 5, 6.5], [10, 5, 8]]




def is_triangle(a, b, c):
    if a < b + c and a > b - c and a > c - b:
        return True
    return False



def area(a, b, c):
    p = (a + b + c) / 2
    pa = p - a
    pb = p - b
    pc = p - c
    S = p*(pa*pb*pc)
    S = math.sqrt(S)
    return S


def is_pythagorian(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False


def max_area(triangles):
    max_triangle = triangles[0]
    
    for triangle in triangles:
        if area(triangle[0], triangle[1], triangle[2]) > area(max_triangle[0], max_triangle[1], max_triangle[2]):
            max_triangle = triangle
        
    return max_triangle




print(area(10,5,7))
print(area(10,5,6.5))

    
print(max_area(triangles))
