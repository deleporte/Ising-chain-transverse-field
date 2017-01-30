import numpy as np
import scipy.linalg

def xdimers_matrix(J,N):
    """Returns the matrix of the hamiltonian in the space of dimers along x"""
    n=int(N/2)
    M=np.zeros((n+1,n+1))
    for k in range(n+1):
        M[k,k]=float((1.-J)*(4*k-N)) #transverse field
    for k in range(n):
        M[k,k+1]=float(J)*np.sqrt((N-2*k)*(N-2*k-1))/np.sqrt(N-k-1) #Ising
        M[k+1,k]=float(J)*np.sqrt((N-2*k)*(N-2*k-1))/np.sqrt(N-k-1)
    return M

def approxdiag_xdimers(J,N):
    return sorted(scipy.linalg.eigvals(xdimers_matrix(J,N)))

def track_angle(J):
    if J<=1./3.:
        return np.pi/2.;
    else:
        return np.arcsin((1.-J)/(J*2.))

def trackdimers_matrix(J,N):
    theta=track_angle(J)
    n=int(N/2)
    M=np.zeros((n+1,n+1))
    for k in range(n+1):
        M[k,k]=float((1.-J)*(4*k-N))*np.sin(theta) #transverse field contrib
        M[k,k]-= float(J)*np.cos(theta)**2/(N-k-1.)*(-5.*N*k+8.*k*k+N*N-N)#Ising
    for k in range(n):
        M[k,k+1]=float(J)*np.sqrt((N-2*k)*(N-2*k-1))/np.sqrt(N-k-1) #Ising
        M[k,k+1]=M[k,k+1]*(np.sin(theta)**2)
        M[k+1,k]=M[k,k+1]
    return M

def approxdiag_trackdimers(J,N):
    return sorted(scipy.linalg.eigvalsh(trackdimers_matrix(J,N)))

def onedimer_matrix(J,N):
    M=np.zeros((2*N-2,2*N-2))
    for k in range(N): #without dimer
        M[k,k]=-J*((N-2*k)**2-N)/(N-1) #Ising
        M[k,k+1]=(1.-J)*np.sqrt((k+1)*(N-k)) #Transverse field
        M[k+1,k]=M[k,k+1]
    M[N,N]=-J*N
    for k in range(N-3): #with dimer
        M[N+k+1,N+k+1]=-J*((N-2*k-2)*(N-2*k-4)/(N-2)-4*(k+1)*(k+2)/(N-1)) #Ising
        if k<N-4:
            M[N+k+1,N+k+2]=(1.-J)*np.sqrt((k+1)*(N-k-4))
            M[N+k+2,N+k+1]=M[N+k+1,N+k+2]
        #Ising interaction between dimer and non-dimer
        M[N+k+1,k+2]=-4.*J/(N-1)*np.sqrt((N-k-2)*(N-k-3)*(k+2)*(k+1)/(N-2))
        M[k+2,N+k+1]=M[N+k+1,k+2]
    return M

def approxdiag_onedimer(J,N):
    return sorted(scipy.linalg.eigvalsh(onedimer_matrix(J,N)))
