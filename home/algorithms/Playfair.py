import string

def matrix_clave(clave):
    abc = string.ascii_lowercase.replace('j','')
    matriz = [''for i in range(5)]
    i=0
    j=0
    for c in clave:
        if c in abc:
            matriz[i]+=c
            abc=abc.replace(c,'')
            j+=1
            if j>4:
                i+=1
                j=0
    for c in abc:
        matriz[i]+=c
        abc=abc.replace(c,'')
        j+=1
        if j>4:
            i+=1
            j=0
    return matriz

def DesencriptarPlayfair(clave,cifrado):
    clave=clave.lower()
    clave=clave.replace(' ','')
    matriz =  matrix_clave(clave)
    cifrado = cifrado.lower()
    cifrado=cifrado.replace(' ','')
    texto=[]
    pares=[]
    i=0
    while (i<len(cifrado)):
        a = cifrado[i]
        b = cifrado[i+1]
        pares.append(a+b)
        i+=2
    for par in pares:
        f = False
        c1 = par[0]
        c2 = par[1]
        for fila in matriz:
            if c1 in fila and c2 in fila:
                m1 = fila.find(c1)
                m2 = fila.find(c2)
                text = fila[(m1+4)%5]+fila[(m2+4)%5]
                texto.append(text)
                f = True
        if f:
            continue
        for j in range(5):
            col ="".join([matriz[i][j] for i in range(5)])
            if c1 in col and c2 in col:
                m1 = col.find(c1)
                m2 = col.find(c2)
                text = col[(m1+4)%5]+col[(m2+4)%5]
                texto.append(text)
                f = True
        if f:
            continue
        i0=0
        i1=0
        j0=0
        j1=0
        for i in range(5):
            fila = matriz[i]
            if c1 in fila:
                i0=i
                j0=fila.find(c1)
            if c2 in fila:
                i1=i
                j1=fila.find(c2)
        text = matriz[i0][j1]+matriz[i1][j0]
        texto.append(text)
    #print('Texto: '+"".join(texto))
    txt = "".join(texto)
    return txt
    #print(texto)
    

#DesencriptarPlayfair(clav,cifrad)

























            






