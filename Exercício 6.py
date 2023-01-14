# Faça um programa que calcule a raiz quadrada de um número. 
# O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada do número inserido.
from math import sqrt

numero = int(input('Informe um número para calcular a raiz quadrada: '))
print(f'A raiz quadrada do {numero} é: {sqrt(numero)}')