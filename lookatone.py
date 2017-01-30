def guessnearone(J,N):
    values=[]
    #for k1 in range(N):
    #    for k2 in range(N):
    #        values.append(J*(4-N)+(np.cos(np.pi*2*k1/N)+np.cos(np.pi*2*k2/N))*2*(1.-J))
    for k in range(N-1):
        values.append(J*(4-N)+np.cos(np.pi*2*(k+0.5)/N)*4*(1-J))
    return values
