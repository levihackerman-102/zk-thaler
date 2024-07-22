import random
import galois
import numpy as np

n = 2
field_order = 11
GF = galois.GF(field_order)

def mat_nxn(size):
    return GF.Random((size, size))

def vec_nx1(size):
    return [random.randrange(0, field_order) for i in range(size)]

def verify(A, B, C):
    x = GF(vec_nx1(n))
    Cx = C @ x
    ABx = A @ (B @ x)
    
    return (Cx == ABx).all()

if __name__ == "__main__":
    A = mat_nxn(n)
    B = mat_nxn(n)
    print(f"A = \n{A}\nand B = \n{B}\n")
    C_honest = A @ B
    C_malicious = mat_nxn(n)
    print(f"C_honest = \n{C_honest}\nand C_malicious = \n{C_malicious}\n")
    if verify(A,B,C_honest):
        print("C_honest = A*B fr")
    if verify(A,B,C_malicious):
        print("C_malicious = A*B fr")