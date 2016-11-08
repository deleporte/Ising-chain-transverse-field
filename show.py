import matplotlib.pyplot as plt
import time
import scipy.stats

def showexact(N=6,Nb_values=50):
    X=[]
    Y=[]
    t=time.time()
    for enumer in range(0,100):
        J=0.01*float(enumer)
        values=exactdiag(J=J,N=N,Nb_values=Nb_values)
        for val in values:
            X.append(J)
            Y.append(val)
    print(time.time()-t)
    plt.plot(X,Y,'ro')
    plt.axis([0,1,-N,max(Y)])
    plt.show()

def exactvsconstant(N=6,Nb_values=50):
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
    
def exactvsxdimers(N=6,Nb_values=50):
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
        values=approxdiag_xdimers(J,N)
        for val in values:
            Xappr.append(J)
            Yappr.append(val)
    plt.plot(X,Y,'ro')
    plt.plot(Xappr,Yappr,'bo')
    plt.axis([0,1,-N,max(Y)])
    plt.show()

def exactvstrackdimers(N=6,Nb_values=50):
    X=[]
    Y=[]
    Xappr=[]
    Yappr=[]
    for enumer in range(0,100):
        J=0.004*float(enumer)
        values=exactdiag_cpp(J=J,N=N,Nb_values=Nb_values)
        for val in values:
            X.append(J)
            Y.append(val)
        values=approxdiag_trackdimers(J,N)
        for val in values:
            Xappr.append(J)
            Yappr.append(val)
    plt.plot(X,Y,'ro')
    plt.plot(Xappr,Yappr,'bo')
    plt.axis([0,1,-N,max(Y)])
    plt.show()

def diff(N=10):
    X=[]
    Y=[]
    for enumer in range(0,100):
        J=0.01*float(enumer)+0.0005363
        exval=exactdiag_cpp(J,N,10)[0]
        apval=approxdiag_trackdimers(J,N)[0]
        X.append(J)
        Y.append(np.log(apval-exval))
    plt.plot(X,Y,'ro')
    plt.show()

def xdimersvsconstant(N=6,Nb_values=50):
    X=[]
    Y=[]
    Xappr=[]
    Yappr=[]
    for enumer in range(0,100):
        J=0.01*float(enumer)
        values=approxdiag_xdimers(J=J,N=N)
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


def all(N=6,Nb_values=50):
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    X=[]
    Y=[]
    h, =ax.plot(X,Y,'ro')
    Xcs=[]
    Ycs=[]
    hcs, = ax.plot(Xcs,Ycs,'bo')
    Xdm=[]
    Ydm=[]
    hdm, = ax.plot(Xdm,Ydm,'go')
    plt.axis([0,1,-N,0])
    plt.show()
    for enumer in range(0,100):
        J=0.01*float(enumer)+0.0001
        values=approxdiag_trackdimers(J,N)
        for val in values:
            Xdm.append(J)
            hdm.set_xdata(Xdm)
            Ydm.append(val)
            hdm.set_ydata(Ydm)
        values=approxdiag_constant(J,N)
        for val in values:
            Xcs.append(J)
            hcs.set_xdata(Xcs)
            Ycs.append(val)
            hcs.set_ydata(Ycs)
        #values=exactdiag_cpp(J,N,Nb_values)
        for val in exactdiag_cpp(J,N,Nb_values):
            X.append(J)
            h.set_xdata(X)
            Y.append(val)
            h.set_ydata(Y)
        plt.draw()
    ## plt.draw()
    ## plt.plot(X,Y,'ro')
    ## plt.plot(Xcs,Ycs,'bo')
    ## plt.plot(Xdm,Ydm,'go')
    ## plt.axis([0,1,-N,max(Y)])
    ## plt.show()

def log(N=6):
    X=[]
    Rcs=[]
    Rdm=[]
    Rtb=[]
    for enumer in range(1,100):
        J=0.001*float(enumer)
        ref=exactdiag_cpp(J,N,10)[0]
        valcs=approxdiag_constant(J,N)[0]
        valdm=approxdiag_trackdimers(J,N)[0]
        valtb=approxdiag_turnedblock(J,N)[0]
        X.append(np.log(J))
        Rcs.append(np.log(valcs-ref))
        Rdm.append(np.log(valdm-ref))
        Rtb.append(np.log(valtb-ref))
    print scipy.stats.linregress(X,Rcs)
    print scipy.stats.linregress(X,Rdm)
    print scipy.stats.linregress(X,Rtb)
    plt.plot(X,Rcs,'bo')
    plt.plot(X,Rdm,'go')
    plt.plot(X,Rtb,'ro')
    #plt.axis([0,1,-N,max()])
    plt.show()

def trackdimersvsturnedblocks(N=6):
    X=[]
    Ydm=[]
    Ytb=[]
    for enumer in range(1,100):
        J=0.005*float(enumer)
        X.append(J)
        Ydm.append(approxdiag_trackdimers(J,N)[0])
        Ytb.append(approxdiag_turnedblock(J,N)[0])
    plt.plot(X,Ydm,'bo')
    plt.plot(X,Ytb,'go')
    #plt.axis([0,1,-N,max()])
    plt.show()
