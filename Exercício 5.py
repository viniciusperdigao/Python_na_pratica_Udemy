# Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma:

# "A média das notas [nota1] e [nota2] é [média]"


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira segunda: '))

media = ( nota1 + nota2) / 2

print(f'A média das notas {nota1} e {nota2} é {media}')