# Escreva um programa que peça um número do usuário e calcule o logaritmo deste número nas bases 10 e 2.

# Dica: utilize o módulo math.

import math

numero = int(input('Digite um numero inteiro:'))

print(f'O logaritimo do número {numero} na base 10 é: {math.log10(numero)} e na base 2 é: {math.log2(numero)}')