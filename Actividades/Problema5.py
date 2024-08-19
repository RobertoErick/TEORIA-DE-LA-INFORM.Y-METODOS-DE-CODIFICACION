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

print("==========")
print("Problema 5")
print("==========")
print("En ocho lanzamientos de una moneda justa, encunetree la probabilidad de que caiga cara \na) Exactamente 3 veces \nb) Al menos 3 veces \nc) A lo mucho 3 veces")

n = 8   # Número de lanzamientos
p = 0.5 # Probabilidad de que salga cara
k = 3   # Eventos que nos interesan

# a) Probabilidad de que caiga cara exactamente 3 veces
prob_exactly_k = binomial_probability(n, p, k)
print(f"Probabilidad de que caiga cara exactamente {k} veces: {prob_exactly_k:.4f}")

# b) Probabilidad de que caiga cara al menos 3 veces
prob_at_least_k = at_least_k(n, p, k)
print(f"Probabilidad de que caiga cara al menos {k} veces: {prob_at_least_k:.4f}")

# c) Probabilidad de que caiga cara a lo mucho 3 veces
prob_at_most_k = at_most_k(n, p, k)
print(f"Probabilidad de que caiga cara a lo mucho {k} veces: {prob_at_most_k:.4f}")
