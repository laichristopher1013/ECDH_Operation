#y^2 = x^3 + ax + b
#ECC (elliptic curve operation)
    #check (check p is on the ecc or not) 
    #findinverse (find the inverse of the given point)
    #findcoord (find the coordinates of giving x on the curve)
    #findN (find the quantity of all the points thats on the curve)
    #findn (find the order of the given generated point)
    #add (modadd) 
    #mul (montgomary ladder) 

class ECC:
    def __init__(self, a, b, p):
        self.zero = None
        self.a = a
        self.b = b
        self.p = p

    def check(self, p):
        if p == self.zero:
            return True

        x, y = p

        if not (0 <= x < self.p and 0 <= y < self.p) or \
        not (x**3 + (self.a * x) + self.b - y**2) % self.p == 0:
            raise ValueError("Invalid point")
        return True

    def findinverse(self, p):
        self.check(p)
        x, y = p
        return(x, -y % self.p)

    def findcoord(self, x):
        if x < self.p:
            n = (x**3 + (self.a * x) + self.b) % self.p

            for i in range(0, self.p):
                if i**2 % self.p == n:
                    return((x, i), (x, -i % self.p))
            raise ValueError("Not found")
        else:
            raise ValueError("Out of range")

    def findN(self):
        count = 1 
        for x in range(self.p):
            try:
                p1, p2 = self.findcoord(x)
                if p1 == p2:
                    count += 1
                else:
                    count += 2
            except Exception:
                pass
        return count

    def findn(self, g): 
        self.check(g)
        for i in range(1, self.findN() + 1):
            if self.mul(g, i) == self.zero:
                return i
        raise ValueError("Invalid order") 

    def add(self, p1, p2):
        self.check(p1)
        self.check(p2)
        if p1 == self.zero:
            return p2
        elif p2 == self.zero:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 and (y1 + y2) % self.p == 0:
            return self.zero
        elif (x1, y1) == (x2, y2):
            m = ((x1**2 * 3 + self.a) * pow((y1 * 2), -1, self.p)) % self.p
        else:
            m = ((y1 - y2) * pow((x1 - x2), -1, self.p)) % self.p

        x3 = (m**2 - (x1 + x2)) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def mul(self, g, n): 
        self.check(g)
        r0 = self.zero
        r1 = g

        for i in bin(n)[2:]:
            if i == "1":
                r0 = self.add(r0, r1)
                r1 = self.add(r1, r1)
            else:
                r1 = self.add(r1, r0)
                r0 = self.add(r0, r0)
        
        return r0

if __name__ == "__main__":
    g = (5, 1) 
    n = 5
    a, b, p = 2, 2, 17 
    x, y = g
    ecc = ECC(a=a, b=b, p=p) 
    print("-------------------------------------------\n") 
    print(f"ECC Curve: y^2 = x^3 + {a}x + {b} mod({p})")
    print(f"G: {g}\n" )
    print(f"G Inverse: {ecc.findinverse(g)}") 
    print(f"Coordinates x = {x}: {ecc.findcoord(x)}") 
    print(f"N: {ecc.findN()}") 
    print(f"n: {ecc.findn(g)}") 
    print(f"h: {ecc.findN()/ecc.findn(g)}")
    print(f"{n}G: {ecc.mul(g, n)}") 
    print("\n-------------------------------------------") 