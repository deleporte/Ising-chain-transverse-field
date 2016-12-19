def lam(N=6,k=0,J=0):
    if k==N/2:
        return (-J*2+1)*2
    else:
        return 2.*np.sqrt(np.cos(np.pi*2.*k/N)*2*J*(1-J)+1-2*J+2*J*J)

def fermions(J=0,N=6):
    eigs=[]
    for i in range(2**N):
        state=digits(2,i)
        while len(state)<N:
            state.append(0)
        value=0
        #odd states
        if (bool(sum(state)%2)):
            for k in range(N):
                value += lam(N,k,J)*(state[k]-0.5)
        #even states
        if not sum(state)%2:
            for k in range(N):
                value += lam(N,0.5+k,J)*(state[k]-0.5)
        eigs.append(value)
    return eigs

def exact_two_fermions(J=0,N=6):
    eigs=[]
    value=0
    for k in range(N):
        value += lam(N,0.5+k,J)*(-0.5)
    eigs.append(value)
    value=lam(N,N/2,J)
    for k in range(N):
        value += lam(N,k,J)*(-0.5)
    eigs.append(value)
    return eigs
