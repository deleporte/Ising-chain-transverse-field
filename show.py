import matplotlib.pyplot as plt

def showexact(N=6,Nb_values=50):
    X=[]
    Y=[]
    for enumer in range(0,100):
        J=0.01*float(enumer)
        values=exactdiag(J=J,N=N,Nb_values=Nb_values)
        for val in values:
            X.append(J)
            Y.append(val)
    plt.plot(X,Y,'ro')
    plt.axis([0,1,-N,max(Y)])
    plt.show()

def comparewithconstant(N=6,Nb_values=50):
    X=[]
    Y=[]
    Xappr=[]
    Yappr=[]
    for enumer in range(0,100):
        J=0.01*float(enumer)
        values=exactdiag(J=J,N=N,Nb_values=Nb_values)
        for val in values:
            X.append(J)
            Y.append(val)
        values=approxdiag_constant(J,N)
        for val in values:
            Xappr.append(J)
            Yappr.append(val)
    plt.plot(X,Y,'ro')
    plt.plot(Xappr,Yappr,'bo')
    plt.axis([0,1,-N,max(Y)])
    plt.show()
    
