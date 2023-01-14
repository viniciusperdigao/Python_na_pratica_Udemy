# Faça um programa que peça 5 números de ponto flutuante do usuário e apresente no final a média dos números digitados.
lista_numeros = []
for i in range (0,5):
    numero = float(input('Digite um número: '))
    lista_numeros.append(numero)

print(f'A média dos números digitados é: {sum(lista_numeros)/len(lista_numeros)}')