from mpi4py import MPI
import numpy as np 
import time
import sys
""" import sistemske biblioteke sys zbog sys.exit() i sys.argv uz pomoć 
kojeg smo iz komandne linije uzeli paramtetar za dimenziju kreiranja matrice """



def kreiranjeMatrice(dimenzija):
    """
    Description:
        Funkcija kreiranjeMatrice služi za kreiranje n-dimenzionalne matrice.

    Args:
        dimenzija (int): dimenzija n-dimenzionalne matrice (broj redaka, stupaca).

    Returns:
        matrica (np.int64): kreirana matrica tipa np.int64.
    """
    matrica = np.random.randint(10, size=(dimenzija, dimenzija))
    return matrica



def mnozenjeMatrice(dimenzija, matrA, matrB):
    """
    Description:
        Funkcija mnozenjeMatrice je funkcija uz pomoć koje se množe matrice.

    Args:
        dimenzija (int): dimenzija n-dimenzionalne matrice (broj redaka, stupaca).
        matrA (np.int64): prva od ukupno dvije matrice koje se množe unutar funkcije.
        matrB (np.int64): druga od ukupno dvije matrice koje se množe unutar funkcije.

    Returns:
        rezultatMnozenja (np.int64): konačni rezultat množenja.
    """
    rezultatMnozenja = np.empty((dimenzija,dimenzija),dtype=np.int64)
    for i in range(dimenzija):
        for j in range(dimenzija):
            rezultatMnozenja[i][j] = matrA[i][j] * matrB[i][j]
    return rezultatMnozenja




comm = MPI.COMM_WORLD
rank = comm.Get_rank() 
size = comm.Get_size()




if size < 3:
    sys.exit("Program je potrebno pokrenuti s najmanje tri procesa.")
""" provjera broja procesa je nužna budući da se program izvršava s najmanje
tri procesa, a ukoliko ih je više, oni se ignoriraju te se unutar njih poziva sys.exit()"""


zadanaDimenzija = int(sys.argv[1])
# iniciramo varijablu zadanaDimenzija u koju spremamo drugi parametar unosa na komandnoj liniji



if rank==0:

    matricaA = kreiranjeMatrice(zadanaDimenzija) # matricaA je prva matrica koja se kreira pozivanjem ranije definirane funkcije kreiranjeMatrice
    matricaB = kreiranjeMatrice(zadanaDimenzija) # matricaB je druga matrica koja se kreira pozivanjem ranije definirane funkcije kreiranjeMatrice


    porukaA = matricaA # iniciramo varijablu porukaA kojoj pridružujemo ranije kreiranu matricuA
    comm.Send(porukaA, dest=1) # slanje varijable porukaA na proces ranka 1
    porukaB = matricaB # iniciriamo varijablu porukaB kojoj pridružujemo ranije kreiranu matricuB
    comm.Send(porukaB, dest=1) # slanje varijable porukaB na proces ranka 1


    print("Matrica A: \n", porukaA) # ispis prve matrice
    print("Matrica B: \n", porukaB) # ispis druge matrice
    
    

elif rank==1:

    primljenaPorukaA = np.empty((zadanaDimenzija,zadanaDimenzija), dtype=np.int64) # iniciramo varijablu primljenaPorukaA u kojoj alociramo prazno numpy polje veličine zadane dimenzije tipa np.int64
    comm.Recv(primljenaPorukaA, source=0) # primanje varijable primljenaPorukaA s procesa ranka 0
    primljenaPorukaB = np.empty((zadanaDimenzija,zadanaDimenzija), dtype=np.int64) # iniciramo varijablu primljenaPorukaB u kojoj alociramo prazno numpy polje veličine zadane dimenzije tipa np.int64
    comm.Recv(primljenaPorukaB, source=0) # primanje varijable primljenaPorukaB s procesa ranka 0


    umnozakMatrica = mnozenjeMatrice(zadanaDimenzija, primljenaPorukaA, primljenaPorukaB) # umnozakMatrice je varijabla u kojoj spremamo rezultat množenja koji nam je vratila ranije definirana funkcija mnozenjeMatrice
    comm.Send(umnozakMatrica, dest=2) # slanje varijablje umnozakMatrica na proces ranka 2


elif rank==2:

    rezultat = np.empty((zadanaDimenzija,zadanaDimenzija), dtype=np.int64) # iniciramo varijablu rezultat u kojoj alociramo prazno numpy polje veličine zadane dimenzije tipa np.int64
    comm.Recv(rezultat, source=1) # primanje varijable rezultat s procesa ranka 1



    time.sleep(2) # spavanje programa kako bi simulirali trajanje izračuna
    print("Rezultat množenja: \n", rezultat) # ispis rezultata množenja matrice


else:
    sys.exit() # izlaz na procesima koji imaju rang veći od 2 budući da je programu potrebno samo tri procesa za izračun umnoška




    




