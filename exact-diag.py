import numpy as np
import scipy.sparse
import scipy.sparse.linalg

def exactdiag(J=1, N=6, Nb_values=50, Find_vectors=False):
    #runtime : tractable for N<=10
    #needs portation to armadillo
    #building the csr sparse matrix
    shape=(2**int(N),2**int(N))
    data=[]
    row_ind=[]
    col_ind=[]
    for i in range(2**(int(N))):
        state=digits(2,i)
        while len(state)<int(N):
            state.append(0)
        value=0.
        for j in range(int(N)):
            value -= float(J)*(2.*state[j]-1.)*(2.*state[(j+1)%int(N)]-1.)
            varstate=state[:]
            varstate[j]=1-varstate[j]
            col_ind.append(i)
            row_ind.append(number(2,varstate))
            data.append(1.-float(J))
        data.append(value)
        col_ind.append(i)
        row_ind.append(i)
    M=scipy.sparse.csr_matrix((data,(row_ind,col_ind)),shape)
    #diagonalization
    pack=scipy.sparse.linalg.eigsh(M,k=min(2**(int(N))-1,Nb_values),
                                   return_eigenvectors=Find_vectors,
                                   sigma = -int(N)-1.)
    if Find_vectors:
        values=np.real(pack[0])
        vectors=pack[1]
        return values,vectors
    else:
        values=np.real(pack)
        return values


def number(base,digits):
    result=0
    temp=digits[:]
    while len(temp) != 0:
        result *= base
        result += temp.pop()
    return result

def digits(base,number):
    digits=[]
    N=int(number)
    while N > 0:
        digits.append(N-base*int(N/base))
        N /= base
    return digits
