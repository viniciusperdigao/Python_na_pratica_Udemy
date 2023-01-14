# Escreva um programa que faça a conversão de um dado valor de metro para quilômetro.

def metro_km(km):
    metro = km / 1000 
    return metro

quilometros = float(input('Digite a quantidade de KM para converter para Metros: '))
print(f'O valor de {quilometros} m em KM é: {metro_km(quilometros)} km.')