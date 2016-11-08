import scipy.linalg
import numpy as np

def approxdiag_turnedblock(J=0.,N=6):
    M=np.zeros((N+1,N+1))
    for n in range(N+1):
        M[n,n]=(1.-J)*(2.*n-N)
    M[0,2]=np.sqrt(N)*J
    M[2,0]=M[0,2]
    M[N-2,N]=float(J)
    M[N,N-2]=float(J)
    M[1,1]+=float(J)*2.
    M[N-1,N-1]+=float(J)*2.
    for n in range(N-3):
        M[n+1,n+3]=float(J)*2.
        M[n+3,n+1]=float(J)*2.
    return sorted(scipy.linalg.eigvalsh(M))
