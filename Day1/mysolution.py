def calcular_fuel(numero):
    nueva_masa = int(int(numero)/3) - 2
    if nueva_masa > 0:
        return nueva_masa + calcular_fuel(nueva_masa)
    else:
        return 0

total = 0

with open("entrada.txt", "r") as entrada:
    for valor in entrada.readlines():
        fuel = calcular_fuel(valor)
        total += fuel
print("Se necesita " + str(total) + " combustible")
