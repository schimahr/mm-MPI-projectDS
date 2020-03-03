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


if rank==0:
    vektori = np.random.randint(10, size=size) * 1j # Inicijalizacija vektora kompleksnih brojeva
else:
    vektori = np.empty(size, dtype=np.complex)

data = comm.bcast(vektori, root=0)


if rank in range(size): # Svaki rank unutar broja procesa izvodi izračun Diskretne Fourieove transformacije
    izracun = DFT(vektori)
    primljeniVektor = np.empty(size, dtype=np.complex)

if rank==0:
    primljeniRezultat = np.empty((size,size), dtype=np.complex) # Iniciramo praznu matricu u koju će primiti sva rješenja
else:
    primljeniRezultat = None

newData = comm.gather(izracun, root=0) # Gather na kojem prikupljamo sva rješenja s procesa na proces ranka 0

comm.Scatter(primljeniRezultat, primljeniVektor, root=0) # Scatteramo rješenja nazad svojim procesima


if rank == 0:
    print("Trajanje programa: ", (time.time()-vrijemePocetka))



