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
    vektori = np.random.randint(10, size=(size,size)) * 1j # Inicijalizacija vektora kompleksnih brojeva
    porukaVektori = vektori
    suma = np.empty((size,size), dtype=np.complex)
else:
    porukaVektori = None

primljeniVektor = np.empty(size, dtype=np.complex)
data = comm.Scatter(porukaVektori, primljeniVektor, root=0) # Raspršivanje redova matrice po procesima

if rank in range(size): # Svaki rank unutar broja procesa izvodi izračun Diskretne Fourieove transformacije
    izracun = DFT(primljeniVektor)


if rank == 0:
    primljeniRezultati = np.empty((size,size), dtype=np.complex)
else:
    primljeniRezultati = None

newData = comm.gather(izracun, root=0) # Skupljanje pojedinačno izračunatih vektora u jedno polje

if rank == 0:
    print("Trajanje programa: ", (time.time()-vrijemePocetka)) # Ispis trajanja programa


