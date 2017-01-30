import numpy as np
import scipy
import random
import matplotlib.pyplot as plt

def Euler(f,x,dt):
    y=x.copy()
    for k in range(len(x)):
        y[k] += dt*f(x)[k]
    return y

def RK4(f,x, dt):
    """Implementation of RK4 algorithm.
    
    Input:
    A vector field f
    An R2-valued vector x
    The time step dt

    Output:
    The flow of x by f at time d+dt."""

    y=x.copy()
    k1=dt*f(x)
    k2=dt*f(x+k1*0.5)
    k3=dt*f(x+k2*0.5)
    k4=dt*f(x+k3)
    return x+k1/6+k2/3+k3/3+k4/6
    return y


def field(J,x):
    """The hamiltonian field.

    Input:
    An R2-valued vector x
    A float J

    Output:
    The value of the field at x
    """
    N=len(x)
    f=np.zeros((N,2))
    for k in range(N):
        f[k,0]=-(1.-J)*np.sin(x[k,1])
        f[k,1]=J*(np.cos(x[(k-1)%N,0])+np.cos(x[(k+1)%N,0]))
        f[k,1]-=(1.-J)*np.cos(x[k,0])/np.sin(x[k,0])*np.cos(x[k,1])

    return f

def Sobonorm(x,s): #OK
    """The squared s semisobolev norm of x.

    Input:
    An R3-valued vector x
    The parameter s

    Output:
    A positive float.
    """
    norm=0
    N=len(x)
    for k in range(N-1):
        #compute the k-th Fourier mode
        c=np.array([0,0,0],dtype=complex)
        for i in range(N):
           c += 1./np.sqrt(N)*np.exp(np.pi*2*1j*(k+1)*i/N)*x[i]
        #add its norm
        norm += (min(k+1,N-k-1))**s*np.real(c.dot(c.conj()))
    return norm

def R3coords(x): #OK
    """From polar coordinates to coordinates in R3.

    Input: An R2-valued vector x
    Output: An R3-valued vector"""
    return np.array([list(np.sin(x.T[0])*np.cos(x.T[1])),list(np.sin(x.T[0])*np.sin(x.T[1])),list(np.cos(x.T[0]))]).T


def Init(N,delta,s):  #OK
    """Generates a starting point with small Sobolev norm.
    Input: 
    An integer N
    A float delta
    A float s

    Return:
    An R2 valued vector
    """
    theta0=random.random()*np.pi
    phi0=random.random()*np.pi*2
    #Fourier components
    v=[]
    for k in range(N-1):
        v.append([random.random()+random.random()*1j,random.random()+random.random()*1j])
    #Generate the resulting vector
    x=[]
    for i in range(N):
        theta=theta0
        phi=phi0
        for k in range(N-1):
            theta += delta/np.sqrt(N)*np.exp(np.pi*2*k*i*1j/N)*(min(k+1,N-k-1))**(-s)*v[k][0]
            phi += delta/np.sqrt(N)*np.exp(np.pi*2*k*i*1j/N)*(min(k+1,N-k-1))**(-s)*v[k][1]
        x.append([np.real(theta),np.real(phi)])
    print Sobonorm(R3coords(np.array(x)),s)
    return np.array(x)

def evolve(N,J,dt,delta,s):
    #Do a movie with it
    #Temporal Fourier Series ?
    at_critpoint=False
    x=Init(N,delta,s)
    t=0.
    T=[]
    Norm=[]
    while t<50.*N and not at_critpoint:
        x=RK4(lambda x:field(J,x),x,dt)
        T.append(t)
        Norm.append(Sobonorm(R3coords(x),s))
        t+=dt
        #Test if all angles are far from one of the critical points
        for k in range(N):
            if np.sin(x[k,0])<10.*dt:
                print "critical theta reached !"
                at_critpoint=True
    print x
    #plt.plot(T,Norm,'bo')
    #plt.show()

    FFT = abs(scipy.fft(Norm[::30]))
    #freqs = scipy.fftpack.fftfreq(len(T), dt)
    plt.subplot(211)
    plt.plot(T,Norm,'bo')
    plt.subplot(212)
    plt.plot(20*np.log(FFT),'bo')
    plt.xlim(-10*N,10*N)
    plt.show()
 
