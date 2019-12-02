import sys

puntero = 0
salida = False
with open("entrada.txt", "r") as entrada:
    cinta_protected = entrada.readline().split(",")

for n1 in range(0, 100):
    for n2 in range(0, 100):
        cinta = cinta_protected.copy()
        cinta[1] = n1
        cinta[2] = n2
        salida = False
        puntero = 0
        while cinta[puntero] != '99' and salida is False:
            if cinta[puntero] == '1':
                cinta[int(cinta[puntero+3])] = int(cinta[int(cinta[puntero+1])]) + int(cinta[int(cinta[puntero+2])])
            elif cinta[puntero] == '2':
                cinta[int(cinta[puntero+3])] = int(cinta[int(cinta[puntero+1])]) * int(cinta[int(cinta[puntero+2])])
            else:
                print("Error en el programa")
                salida = True
            puntero += 4

        if cinta[0] == 19690720:
            print("Encontrado")
            print(n1, n2)
            sys.exit()
