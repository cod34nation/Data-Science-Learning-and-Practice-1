# GLobal Variabel

x = 'Global Variabel'

def varGlob():
    global x #for initiate global variabel
    x = x*2
    print (x)

varGlob()

# Variabel Non Local

def VarNonLocal():
    y = 'non local'

    def innerVar():
        nonlocal y #for initiate non local variabel
        y = 'var non local'
        print(y)
    
    innerVar()

VarNonLocal()