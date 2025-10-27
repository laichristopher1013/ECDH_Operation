from fractions import Fraction as fraction

#the ecc variable
#y^2 = x^3 + ax + b
a, b = -7, 10
p1 = (2, 2)
p2 = (-1, 4)

def normaladd(p1, p2):
    #to unpack the coordinates
    x1, y1 = p1
    x2, y2 = p2

    #coordinates are each other inverse 
    if x1 == x2 and y1 + y2 == 0:
        return None
    #coordinates are the same
    elif (x1, y1) == (x2, y2):
        m = fraction((x1**2 * 3 + a), (y1 * 2))
    #coordinates are different
    else:
        m = fraction((y1 - y2), (x1 - x2))

    #the result of the 2 coordinates adding together 
    x3 = float(m**2 - (x1 + x2))
    y3 = float(m * (x1 - x3) - y1)

    return (x3, y3)

#example
print("\n-------------------------------------------\n") 
print("Normal Add")
print(f"a: {a}, b: {b}")
print(f"p1: {p1}, p2: {p2}")
print(normaladd(p1, p2)) 
print("\n-------------------------------------------\n") 

#the ecc variable
a, b = 2, 2
modp = 17
p1 = (10, 6)
p2 = (6, 3)

def modadd(p1, p2):
    #to unpack the coordinates
    x1, y1 = p1
    x2, y2 = p2
    
    #coordinates are each other inverse 
    if x1 == x2 and y1 + y2 == 0:
        return None
    #coordinates are the same
    elif (x1, y1) == (x2, y2):
        m = ((x1**2 * 3 + a) * pow((y1 * 2), -1, modp)) % modp
    #coordinates are different
    else:
        m = ((y1 - y2) * pow((x1 - x2), -1, modp)) % modp

    #the result of the 2 coordinates adding together 
    x3 = (m**2 - (x1 + x2)) % modp
    y3 = (m * (x1 - x3) - y1) % modp

    return (x3, y3)

#example
print("\n-------------------------------------------\n") 
print("Mod Add")
print(f"a: {a}, b: {b}, modp: {modp}")
print(f"p1: {p1}, p2: {p2}")
print(modadd(p1, p2)) 
print("\n-------------------------------------------\n") 
