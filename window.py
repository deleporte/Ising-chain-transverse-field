from Tkinter import *

def menu():
    root = Tk()

    logvar=BooleanVar()
    logvar.set(False)
    exactvar=StringVar()
    exactvar.set('cpp')
    constantvar=BooleanVar()
    constantvar.set(True)
    tkdimervar=BooleanVar()
    tkdimervar.set(True)
    tdblockvar=BooleanVar()
    tdblockvar.set(True)

    content = Frame(root)

    constantcb=Checkbutton(content, text="Constant fields",
                         variable=constantvar,
                         onvalue=True)
    tkdimercb=Checkbutton(content, text="Neighbour dimers",
                         variable=tkdimervar,
                         onvalue=True)
    tdblockcb=Checkbutton(content, text="Upturned block",
                         variable=tdblockvar,
                         onvalue=True)

    logrb=Radiobutton(content, text='show log of ratio',
                      variable=logvar, value=True)
    valrb=Radiobutton(content, text='show exact and approximated values',
                      variable=logvar, value=False)

    cpprb=Radiobutton(content, text='numerics with c++',
                      variable=exactvar, value='cpp')
    pyrb=Radiobutton(content, text='numerics with python',
                     variable=exactvar, value='py')
    falrb=Radiobutton(content, text='exact (whole spectrum)',
                      variable=exactvar, value='fal')
    f2rb=Radiobutton(content, text='exact (2 first values)',
                     variable=exactvar, value='f2')
    cplbl=Label(content, text="Compare with:")

    Jmin= StringVar() #TODO
    Jmin.set('0')
    Jmax= StringVar()
    Jmax.set('1')
    Jstep= StringVar()
    Jstep.set('0.01')
    N= StringVar()
    N.set('8')
    Nb_values= StringVar()
    Nb_values.set('10')
    
    Jminen=Entry(content, textvariable=Jmin)
    Jminlbl=Label(content, text="Jmin")
    Jmaxen=Entry(content, textvariable=Jmax)
    Jmaxlbl=Label(content, text="Jmax")
    Jstepen=Entry(content, textvariable=Jstep)
    Jsteplbl=Label(content, text="step for J")
    Nen=Entry(content, textvariable=N)
    Nlbl=Label(content, text="N")
    Nb_valuesen=Entry(content, textvariable=Nb_values)
    Nb_valueslbl=Label(content, text="Nb of values")

    compute=Button(content, text="Compute !", command=lambda: draw(
        logvar.get(),N.get(),Jmin.get(),Jmax.get(),Jstep.get(),Nb_values.get(),
        exactvar.get(),constantvar.get(),tkdimervar.get(),tdblockvar.get()))
    
    
    
    content.grid(column=0, row=0)
    cpprb.grid(column=0,row=0)
    pyrb.grid(column=0,row=1)
    falrb.grid(column=0,row=2)
    f2rb.grid(column=0,row=3)
    logrb.grid(column=1,row=0)
    valrb.grid(column=1,row=1,columnspan=2)
    cplbl.grid(column=0,row=4,columnspan=3)
    constantcb.grid(column=0,row=5)
    tkdimercb.grid(column=1,row=5)
    tdblockcb.grid(column=2,row=5)
    Jminlbl.grid(column=3,row=0)
    Jminen.grid(column=4,row=0)
    Jmaxlbl.grid(column=3,row=1)
    Jmaxen.grid(column=4,row=1)
    Jsteplbl.grid(column=3,row=2)
    Jstepen.grid(column=4,row=2)
    Nlbl.grid(column=3,row=3)
    Nen.grid(column=4,row=3)
    Nb_valueslbl.grid(column=3,row=4)
    Nb_valuesen.grid(column=4,row=4)
    compute.grid(column=3,row=5,columnspan=2)
    
    root.mainloop()

def draw(logvar,N,Jmin,Jmax,Jstep,Nb_values,cppvar,constantvar,tkdimervar,
         tdblockvar):
    try:
        if logvar:
            log(int(N),float(Jmin),float(Jmax),
                float(Jstep),
                cppvar,constantvar,tkdimervar,
                tdblockvar)
        else:
            show(int(N),float(Jmin),float(Jmax),
                float(Jstep),
                cppvar,int(Nb_values),
                constantvar,tkdimervar,tdblockvar)
    except ValueError:
        pass
