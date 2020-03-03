import numpy as np
from mpi4py import MPI
import cmath
import time

vrijemePocetka = time.time()

def DFT(vektor):
    """
    Description:
        Funkcija DFT služi za provođenje Diskretne Fourieove transformacije
        nad vektorom nasumičnih kompleksnih brojeva.
    Args:
        vektor(complex): nasumični vektor koji se sastoji od n kompleksnih brojeva.
    Returns:
        transVektor(complex): transformirani vektor.
    """
    n = len(vektor)
    transfVektor = []
    for k in range(n):  
        s = 0.0
        for t in range(n):  
            angle = 2j * cmath.pi * t * k / n
            s += vektor[t] * cmath.exp(-angle)
        transfVektor.append(s)
    return transfVektor

comm = MPI.COMM_WORLD
rank = comm.Get_rank() 
size = comm.Get_size()


vektori = np.random.randint(10, size=size) * 1j
if rank==0:
    vektori = np.random.randint(10, size=size) * 1j # Inicijalizacija vektora kompleksnih brojeva
    print(vektori)
else:
    vektori = None

primljeniVektor = np.empty(1, dtype=np.complex)

comm.Scatter(vektori,primljeniVektor,root=0)
print(primljeniVektor)

if rank in range(size): # Svaki rank unutar broja procesa izvodi izračun Diskretne Fourieove transformacije
    izracun = DFT(primljeniVektor)
    

if rank == 0:
    primljeniVektor2 = np.empty(1, dtype=np.complex)
else:
    primljeniVektor2 = None

comm.Reduce(primljeniVektor,primljeniVektor2, op=MPI.SUM,root=0)
print(primljeniVektor2)

if rank == 0:
    print("Trajanje programa: ", (time.time()-vrijemePocetka))



