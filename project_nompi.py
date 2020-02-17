import numpy as np 
import time
import sys
""" import sistemske biblioteke sys zbog sys.exit() i sys.argv uz pomoć 
kojeg smo iz komandne linije uzeli paramtetar za dimenziju kreiranja matrice """

vrijemePocetka = time.time()


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

zadanaDimenzija = int(sys.argv[1])
# iniciramo varijablu zadanaDimenzija u koju spremamo drugi parametar unosa na komandnoj liniji



matricaA = kreiranjeMatrice(zadanaDimenzija) # matricaA je prva matrica koja se kreira pozivanjem ranije definirane funkcije kreiranjeMatrice
matricaB = kreiranjeMatrice(zadanaDimenzija) # matricaB je druga matrica koja se kreira pozivanjem ranije definirane funkcije kreiranjeMatrice


print("Matrica A: \n", matricaA) # ispis prve matrice
print("Matrica B: \n", matricaB) # ispis druge matrice
    
rezultat = mnozenjeMatrice(zadanaDimenzija,matricaA,matricaB)

print("Rezultat množenja: \n", rezultat) # ispis rezultata množenja matrice

print("Trajanje programa: ", (time.time() - vrijemePocetka))




