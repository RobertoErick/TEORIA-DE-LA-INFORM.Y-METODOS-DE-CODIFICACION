#   Distribcion Binomial
#   Cuenta el número de éxitos en una secuencia de ensayos de Bernoulli independientes entre sí con una probabilidad fija de ocurrencia de éxito entre los ensayos.

from scipy.stats import binom

def binomial_probability(n, p, k):
    #k: Número de eventos deseados exactos

    return binom.pmf(k, n, p)

def at_least_k(n, p, k):
    #k: Número mínimo de éxitos deseados

    return 1 - binom.cdf(k-1, n, p)

def at_most_k(n, p, k):
    #k: Número máximo de éxitos deseados

    return binom.cdf(k, n, p)

print("====================\nDistribcion Binomial\n====================")
print("Cuenta el número de éxitos en una secuencia de ensayos de Bernoulli independientes entre sí con una probabilidad fija de ocurrencia de éxito entre los ensayos.")
print("\nn = ocurrencias del evento \nk = eventos que nos interesan\np = probabilidad")

n = float(input("Ingrea el numero que va a representar a n: "))
p = float(input("Ingrea el numero que va a representar a p: "))
Opcion = int(input("\nComo va a ocurrir el evento que nos importa? \n1) Exactamente k veces \n2) Al menos k veces \n3) A lo mucho k veces \nEscribe el numero de la opcion:"))
if Opcion == 1:
    k = float(input("Ingrea el numero que va a representar a k: "))
    prob_exactly_k = binomial_probability(n, p, k)
    print(f"Probabilidad del evento exactamente {k} veces: {prob_exactly_k:.4f}")
elif Opcion == 2:
    k = float(input("Ingrea el numero que va a representar a k: "))
    prob_at_least_k = at_least_k(n, p, k)
    print(f"Probabilidad del evento al menos {k} veces: {prob_at_least_k:.4f}")
elif Opcion == 3:
    k = float(input("Ingrea el numero que va a representar a k: "))
    prob_at_most_k = at_most_k(n, p, k)
    print(f"Probabilidad del evento a lo mucho {k} veces: {prob_at_most_k:.4f}")
else:
    print("Opcion no valida")