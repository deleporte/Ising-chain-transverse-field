import ctypes

diag = ctypes.CDLL('./exact-diag.so')


def exactdiags_cpp(N=6, samples=100, Nb_values=50):
    #diag.computePackSpectrum.argtypes=(ctypes.c_int, ctypes.c_int,
                                     #ctypes.c_int,
                                     #(ctypes.c_float*(samples*Nb_values))())
    values = (ctypes.c_float*(samples*Nb_values))()
    diag.computePackSpectrum(N, samples, Nb_values, values)
    return values
