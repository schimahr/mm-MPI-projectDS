import numpy as np
from mpi4py import MPI
import cmath
import time
import sys
""" import sistemske biblioteke sys zbog sys.exit() i sys.argv uz pomoć 
kojeg smo iz komandne linije uzeli paramtetar za dimenziju kreiranja matrice """

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


zadanaDimenzija = int(sys.argv[1]) # Dimenziju uzimamo kao drugi argument s komandne linije
vektori = np.random.randint(10, size=(zadanaDimenzija,zadanaDimenzija)) * 1j # Inicijalizacija vektora kompleksnih brojeva

zavrsniRezultat = []

for i in range(zadanaDimenzija):
    izracun = DFT(vektori[i])
    zavrsniRezultat.append(izracun)
    
print("Vrijeme trajanja: ", (time.time()-vrijemePocetka)) # Ispis trajanja programa