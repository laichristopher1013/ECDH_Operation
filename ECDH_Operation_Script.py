#import ECC 
#ECDH (elliptic curve diffie hellman operation) 
    #gen (generate private key & public key) 

from ECC_Operation_Script import ECC 
import random 

class DH:
    def __init__(self, ecc, g):
        self.ecc = ecc 
        self.g = g 
        self.n = self.ecc.findn(self.g) 
    
    def gen(self): 
        pri_k = random.randint(1, self.n - 1) 
        pub_k = self.ecc.mul(self.g, pri_k) 
        return (pri_k, pub_k)

if __name__ == "__main__":
    g = (5, 1)
    a, b, p = 2, 2, 17
    ecc = ECC(a=a, b=b, p=p)
    N, n = ecc.findN(), ecc.findn(g)
    h = N / n
    dh = DH(ecc=ecc, g=g)

    print("-------------------------------------------\n") 
    #generate pri_k, pub_k
    #client 1
    pri_k1, pub_k1 = dh.gen()
    print(f"client 1\n pri_k1: {pri_k1}, pub_k1: {pub_k1}\n")

    #client 2
    pri_k2, pub_k2 = dh.gen()
    print(f"client 2\n pri_k2: {pri_k2}, pub_k2: {pub_k2}\n")

    #deliver pub_k to generate shared key
    #client 1 
    shared_k1 = ecc.mul(pub_k2, pri_k1)
    print(f"client 1: {pub_k2} * {pri_k1}\n shared_k: {shared_k1}\n")

    #client 2
    shared_k2 = ecc.mul(pub_k1, pri_k2)
    print(f"client 2: {pub_k1} * {pri_k2}\n shared_k: {shared_k2}")
    print("\n-------------------------------------------") 