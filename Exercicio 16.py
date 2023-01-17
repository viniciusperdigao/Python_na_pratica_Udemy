# Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.


# Dica: utilize o módulo math do Python, especificamente math.fatorial.

from math import factorial

numero = int(input('Digite um numero inteiro:'))

fatorial = factorial(numero)

print(f'O fatorial de {numero} é: {fatorial}')