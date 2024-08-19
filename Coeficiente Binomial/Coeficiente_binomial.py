#   Coeficiente Binomial
#   Un coeficiente binomial indica cuantos subconjuntos se puede obtener de un conjunto

import math

def coeficiente_binomial(n,k):
    #la funcion devuelve el número de combinaciones sin repetición de n elementos tomados en bloques de k unidades
    #En otras palabras, realiza el coeficiente binomial
    resultado = math.comb(n,k)

    return resultado

print("====================\nCoeficiente Binomial\n====================")
print("Un coeficiente binomial indica cuantos subconjuntos se puede obtener de un conjunto")
print("\nn = Total de elementos \nk = subconjuntos que nos importan")
n = int(input("Ingrese la cantidad de n: "))
k = int(input("ingrese la cantidad de k: "))

resultado = coeficiente_binomial(n,k)
print(f"El resultado del coeficiente binomial de n={n} y k={k} es: {resultado}")