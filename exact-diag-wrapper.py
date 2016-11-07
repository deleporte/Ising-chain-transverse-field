import ctypes
import time

diag = ctypes.CDLL('./exact-diag.so')

def exactdiags_cpp(N=6, samples=100, Nb_values=50):
    #diag.computePackSpectrum.argtypes=(ctypes.c_int, ctypes.c_int,
                                     #ctypes.c_int,
                                     #(ctypes.c_float*(samples*Nb_values))())
    t = time.time()
    CN=ctypes.c_int(N)
    Csamples=ctypes.c_int(samples)
    CNb_values = ctypes.c_int(Nb_values)
    values = (ctypes.c_float*(samples*Nb_values))()
    diag.computePackSpectrum(N, samples, Nb_values, values)
    print(time.time()-t)
    return values

def exactdiag_cpp(J=0.1, N=6, Nb_values=50):
    t = time.time()
    CN=ctypes.c_int(N)
    CJ=ctypes.c_float(J)
    CNb_values = ctypes.c_int(Nb_values)
    values = (ctypes.c_float*Nb_values)()
    diag.computeSpectrum(CN,CJ,CNb_values, values)
    print(time.time()-t)
    return values
