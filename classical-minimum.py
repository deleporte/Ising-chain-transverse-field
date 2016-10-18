import random
import numpy as np

def findclassmin(N=8, J=0.5):
    """A simple gradient descent."""
    DESCENT=0.1
    random.seed()
    at_min=False
    u=[]
    for j in range(N):
        u.append(np.pi/2.*random.random())
    while not at_min:
        grad=[]
        for i in range(N):
            grad.append(-DESCENT*(J*np.sin(u[i])*(np.cos(u[(i+1)%N])
                                                  +np.cos(u[(i+N-1)%N]))
                                  +(1.-J)*np.cos(u[i])))
        if np.sum(r*r for r in grad) < 0.00001*DESCENT*DESCENT:
            at_min=True
        for i in range(N):
            u[i]+=grad[i]

    return u
        
    
    
