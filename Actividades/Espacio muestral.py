import itertools

# Función para calcular el espacio muestral de dos dados
def espacio_muestral_dos_dados():
    dado = [1, 2, 3, 4, 5, 6]
    # Los pares que suman cada valor entre 2 y 12
    combinaciones = [
        (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)
    ]
    return combinaciones

# Función para calcular el espacio muestral de dos dados de diferente color
def espacio_muestral_dos_dados_colores():
    dado_1 = [1, 2, 3, 4, 5, 6]  # Dado de color 1
    dado_2 = [1, 2, 3, 4, 5, 6]  # Dado de color 2
    # Espacio muestral considerando el color y el orden
    espacio_36 = list(itertools.product(dado_1, dado_2))
    return espacio_36

# Calcular y mostrar los resultados
espacio_12 = espacio_muestral_dos_dados()
espacio_36 = espacio_muestral_dos_dados_colores()

print("Espacio muestral de 2 dados (6 combinaciones posibles):")
for resultado in espacio_12:
    print(resultado)

print("\nEspacio muestral de 2 dados de diferente color (36 posibles resultados):")
for resultado in espacio_36:
    print(resultado)

# Imprimir el tamaño de los espacios muestrales
print(f"\nTamaño del espacio muestral de 2 dados: {len(espacio_12)}")
print(f"Tamaño del espacio muestral de 2 dados de diferente color: {len(espacio_36)}")