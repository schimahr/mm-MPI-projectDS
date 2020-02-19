import numpy as np
from mpi4py import MPI
import cmath
import time
import sys

vrijemePocetka = time.time()

def DFT(input):
	n = len(input)
	output = []
	for k in range(n):  
		s = 0.0
		for t in range(n):  
			angle = 2j * cmath.pi * t * k / n
			s += input[t] * cmath.exp(-angle)
		output.append(s)
	return output

zadanaDimenzija = int(sys.argv[1])
vektori = np.random.randint(10, size=(zadanaDimenzija,zadanaDimenzija))

zavrsniRezultat = []

for i in range(zadanaDimenzija):
    izracun = DFT(vektori[i])
    zavrsniRezultat.append(izracun)
    
print("Vrijeme trajanja: ", (time.time()-vrijemePocetka))