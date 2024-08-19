import math

def count_two_pair_hands_with_jokers():
    #Sin utilizar comodines (caso original)
    Cartas_pares = math.comb(13, 2)
    Tipos_De_Cada_Par = math.comb(4, 2)
    Dos_pares = Tipos_De_Cada_Par ** 2
    Quinta_Carta = 11 * 4
    Total_Dos_Pares_en_Mano = Cartas_pares * Dos_pares * Quinta_Carta

    # Considerando las manos donde los dos comodines se utilizan para crear un par adicional
    # Los dos comodines pueden formar un par adicional o ayudar a crear pares existentes
    # Esto se traduce en más combinaciones para los pares.
    # Adicionamos las combinaciones en donde los dos comodines forman el tercer par.
    Total_Dos_Pares_en_Mano += Cartas_pares * 4 * 4 #Posiblemente este mal esta parte

    return Total_Dos_Pares_en_Mano

total_hands = count_two_pair_hands_with_jokers()
print("===========")
print("Actividad 0")
print("===========")
print("¿Cuantas manos diferentes de cinco cartas que contienen dos pares es posible obtener a partir de un deck standard? (contando comodines)")
print(f"El número total de manos con dos pares con 2 comodines es: {total_hands}")
