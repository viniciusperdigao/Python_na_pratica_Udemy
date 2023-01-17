# Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles. A tela de apresentação deverá seguir o seguinte formato:

# "[numero1]x[numero2]=[multiplicação]"

# "[número1]/[numero2]=[divisão]"

numero1 = float(input('Digite o Primeiro Numero: '))
numero2 = float(input('Digite o Segundo Numero: '))

print(f"{numero1} x {numero2} = {numero1 * numero2}")

print(f'{numero1} / {numero2} = {numero1 / numero2}')