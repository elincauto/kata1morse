
simbolos = {
    'A':'·—', 
    'B':'—···', 
    'C': '—·—·', 
    'D': '—··', 
    'E': '·', 
    'F': '··—·',  
    'G': '——·',
    'H': '····', 
    'I': '··',
    'J': '·———',
    'K': '—·—',
    'L': '·—··',
    'M': '——',
    'N': '—·',
    'Ñ': '——·——', 
    'O': '———',
    'P': '·——·',
    'Q': '——·—',
    'R': '·—·', 
    'S': '···',
    'T': '—',
    'U': '··—',
    'V': '···—',
    'W': '·——',
    'X': '—··—',
    'Y': '—·——', 
    'Z': '——··',
    '0': '—————',
    '1': '·————',
    '2': '··———',
    '3': '···——',
    '4': '····—',
    '5': '·····',
    '6': '—····',
    '7': '——···', 
    '8':'———··',
    '9': '————·',
    '.': '·—·—·—',
    ',': '—·—·——',
    '?': '··——··',
    '"': '·—··—·',
    '!': '——··——'}

cadena= "Hola, mundo".upper
for letra in cadena:
    posicion=0
    while posicion < len(letras):
        l = letras[posicion]
        if l==letra:
            break
        posicion +=1
    if posicion==len(letras):
        print("no encontrado")
    else:
        #Obtener letas morse
        pass
        print("{}-{}".format(letra,simbolos[posicion]))