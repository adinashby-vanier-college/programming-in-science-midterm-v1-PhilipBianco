import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 4:
        return "The triangle height should be at least 4." 
    
    result = ""      

    for p in range(n):
        for b in range(p + 1):
            if p == 0 or p == n - 1:
                result += "*"
            elif b == 0 or b == p:
                result += "*"
            else:
                result += " "
        if p < n - 1:
            result += "\n"

    return result

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    if n < 3:
        return "The pyramid height should be at least 3."
    
    result = ""

    for p in range(n):
        result += " " * p
        result += "*" * (2 * (n - p) - 1)
        if p < n - 1:
            result += "\n"

    return result
