import numpy as np
from mpi4py import MPI
import cmath
import time

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

comm = MPI.COMM_WORLD
rank = comm.Get_rank() 
size = comm.Get_size()


if rank==0:
    vektori = np.random.randint(10, size=(size,size))
    porukaVektori = vektori
    suma = np.empty((size,size), dtype=np.complex)
else:
    porukaVektori = None

primiVektore = np.empty(size, dtype=np.int64)
data = comm.Scatter(porukaVektori, primiVektore, root=0)

if rank in range(size):
    izracun = DFT(primiVektore)


if rank == 0:
    primljeniRezultati = np.empty((size,size), dtype=np.complex)
else:
    primljeniRezultati = None

newData = comm.gather(izracun, root=0)

if rank == 0:
    print("Trajanje programa: ", (time.time()-vrijemePocetka))


