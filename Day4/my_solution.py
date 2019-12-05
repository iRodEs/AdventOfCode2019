with open("entrada.txt", "r") as entrada:
    dato = entrada.readline().split("-")

inicio = dato[0]
fin = dato[1]

def parteA(numero):
    stringified = str(numero)

    cagada = False
    double = False
    letra_anterior = -1
    for letra in stringified:
        if int(letra_anterior) <= int(letra):
            if int(letra) == int(letra_anterior):
                double == True
        else:
            cagada = True
        letra_anterior = letra

    if double is True and cagada is False:
        return True
    return False

def parteB(numero):
    stringified = str(numero)

    cagada = False
    double = 0
    letra_anterior = -1
    repeticiones = []
    for letra in stringified:
        if int(letra_anterior) <= int(letra):
            if int(letra) == int(letra_anterior):
                double += 1
            else:
                repeticiones.append(double)
                double = 1
        else:
            cagada = True
        letra_anterior = letra
    repeticiones.append(double)

    if 2 in repeticiones and cagada is False:
        return True
    return False


cont = 0
for i in range(int(inicio), int(fin)+1):
    if parteB(i):
        cont += 1

print(cont)
