# ECDH_Operation 
This whole repository simulate the process of ECDH encryption. 
#### Script: 
* [ECC_Addition_Script.py](https://github.com/laichristopher1013/ECDH_Operation/blob/main/ECC_Addition_Script.py).
* [ECC_Operation_Script.py](https://github.com/laichristopher1013/ECDH_Operation/blob/main/ECC_Operation_Script.py).
* [ECDH_Operation_Script.py](https://github.com/laichristopher1013/ECDH_Operation/blob/main/ECDH_Operation_Script.py).


## ECC_Addition_Script 
This script simulate the process of normal ECC addition `normaladd`, and mod addition `modadd`.

```
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
```
```
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
```
For more detail go: [ECC_Addition_Script.py](https://github.com/laichristopher1013/ECDH_Operation/blob/main/ECC_Addition_Script.py).


## ECC_Operation_Script 
This script simulate the process of ECC operation. It shows how ECC actually works and include bunch of tools such as: find the inverse of a point, find coordinates based on given x, montgomery ladder ecc multiplication, and etc... This script also demonstrate all tools within this ECC script.
```
#ECC (elliptic curve operation)
    #check (check p is on the ecc or not) 
    #findinverse (find the inverse of the given point)
    #findcoord (find the coordinates of giving x on the curve)
    #findN (find the quantity of all the points thats on the curve)
    #findn (find the order of the given generated point)
    #add (modadd) 
    #mul (montgomary ladder)
#example
```
To check actual function go: [ECC_Operation_Script.py](https://github.com/laichristopher1013/ECDH_Operation/blob/main/ECC_Operation_Script.py).


## ECDH_Operation_Script 
This script simulate the process of ECDH encrytion with the previous script "ECC_Operation". It combine the Diffie Hellmen method and ECC operation in order to implement ECDH. This script also provide an example of how to use this ECDH script.

```
#import ECC from ECC_Operation_Script
#ECDH (elliptic curve diffie hellman operation) 
    #gen (generate private key & public key)
#example
```
To check actual function go: [ECDH_Operation_Script.py](https://github.com/laichristopher1013/ECDH_Operation/blob/main/ECDH_Operation_Script.py).
