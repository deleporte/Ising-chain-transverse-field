import numpy as np
import scipy.linalg

def dimers_matrix(J,N):
    """Returns the matrix of the hamiltonian in the space of dimers along x"""
    n=int(N/2)
    M=np.zeros((n+1,n+1))
    for k in range(n+1):
        M[k,k]=float((1.-J)*(4*k-N))
    for k in range(n):
        M[k,k+1]=float(J)*np.sqrt((N-2*k)*(N-2*k-1))/np.sqrt(N-k-1)
        M[k+1,k]=float(J)*np.sqrt((N-2*k)*(N-2*k-1))/np.sqrt(N-k-1)
    return M

def dimerseigs(J,N):
    return sorted(scipy.linalg.eigvals(dimers_matrix(J,N)))
