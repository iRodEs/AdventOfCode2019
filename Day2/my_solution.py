
puntero = 0
salida = False
with open("entrada.txt", "r") as entrada:
    cinta = entrada.readline().split(",")
    while cinta[puntero] != '99' and salida is False:
        if cinta[puntero] == '1':
            cinta[int(cinta[puntero+3])] = int(cinta[int(cinta[puntero+1])]) + int(cinta[int(cinta[puntero+2])])
        elif cinta[puntero] == '2':
            cinta[int(cinta[puntero+3])] = int(cinta[int(cinta[puntero+1])]) * int(cinta[int(cinta[puntero+2])])
        else:
            print("Error en el programa")
            salida = True
        puntero += 4

print("El valor en la posicion 0 es: " + str(cinta[0]))
