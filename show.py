import matplotlib.pyplot as plt
import time
import scipy.stats

exec open("dimers.py")
exec open("exact-diag.py")
exec open("exact-diag-wrapper.py")
exec open("constant-fields.py")
exec open("turned-block.py")


def show(N=6,Jmin=0.,Jmax=1.,Jstep=0.01,cpp=True,Nb_values=10,
         cs=True,dm=True,tb=False):
    plt.ion()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    X=[]
    Y=[]
    h,=ax.plot(X,Y,'ro')
    Xcs=[]
    Ycs=[]
    hcs, =ax.plot(Xcs,Ycs,'bo')
    Xdm=[]
    Ydm=[]
    hdm, =ax.plot(Xdm,Ydm,'go')
    Xtb=[]
    Ytb=[]
    htb, =ax.plot(Xtb,Ytb,'yo')
    plt.axis([Jmin,Jmax,-N,0])
    plt.show()
    for enumer in range(0,int((Jmax-Jmin)/Jstep+1)):
        J=Jmin+Jstep*enumer+0.00001
        if cpp:
            values=exactdiag_cpp(J,N,Nb_values)
        else:
            values=exactdiag(J,N,Nb_values)
        for val in values:
            X.append(J)
            h.set_xdata(X)
            Y.append(val)
            h.set_ydata(Y)
        if cs:
            values=approxdiag_constant(J,N)
            for val in values:
                Xcs.append(J)
                hcs.set_xdata(Xcs)
                Ycs.append(val)
                hcs.set_ydata(Ycs)
        if dm:
            values=approxdiag_trackdimers(J,N)
            for val in values:
                Xdm.append(J)
                hdm.set_xdata(Xdm)
                Ydm.append(val)
                hdm.set_ydata(Ydm)
        if tb:
            values=approxdiag_turnedblock(J,N)
            for val in values:
                Xtb.append(J)
                htb.set_xdata(Xtb)
                Ytb.append(val)
                htb.set_ydata(Ytb)
        print J
        plt.draw()
    

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

def log(N=6,Jmin=0.01,Jmax=0.1,Jstep=0.001,cpp=False,cs=True,dm=True,tb=True):
    X=[]
    Rcs=[]
    Rdm=[]
    Rtb=[]
    for enumer in range(1,int((Jmax-Jmin)/Jstep)):
        J=Jmin+Jstep*float(enumer)
        if cpp:
            ref=exactdiag_cpp(J,N,1)[0]
        else:
            ref=exactdiag(J,N,1)[0]
        valcs=approxdiag_constant(J,N)[0]
        valdm=approxdiag_trackdimers(J,N)[0]
        valtb=approxdiag_turnedblock(J,N)[0]
        if (Jmin-Jmax)/2 < 0.5:
            X.append(np.log(J))
        else:
            X.append(np.log(1.-J))
        Rcs.append(np.log(valcs-ref))
        Rdm.append(np.log(valdm-ref))
        Rtb.append(np.log(valtb-ref))
    if cs:
        plt.plot(X,Rcs,'bo')
    if dm:
        plt.plot(X,Rdm,'go')
    if tb:
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
