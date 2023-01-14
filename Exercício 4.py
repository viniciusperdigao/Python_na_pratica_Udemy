# Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.
lista_numeros = []
for num in range (0,3):
    numero = int(input('Digite um número para ser somado. '))
    lista_numeros.append(numero)

print(f'A soma dos números é {sum(lista_numeros)} ')