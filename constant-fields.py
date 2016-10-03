import scipy.linalg
import numpy as np

def approxdiag_constant(J=1,N=6):
    #building the N+1 square matrix
    M=np.zeros((int(N)+1,int(N)+1),dtype=float)
    for n in range(int(N)):
        M[n,n+1]=(1.-float(J))*np.sqrt((n+1)*(int(N)-n))
        M[n+1,n]=M[n,n+1]
        M[n,n]=-float(J)/(float(N)-1.)*((int(N)-n)*(int(N)-2*n-1)
                                       +n*(2*n-int(N)-1))
    M[N,N]=-float(J)*float(N)
    #diagonalization
    values=sorted(np.real(scipy.linalg.eigvals(M)))
    return values
