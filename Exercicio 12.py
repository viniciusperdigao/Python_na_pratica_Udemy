# Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:

# "Seja bem-vindo [nome] [sobrenome]."

# "Você possui [idade] anos de idade."



# No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e depois da string, enquanto que o último permite colocar a string no formato titlecased (capitaliza a string).

nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
idade = int(input('Digite a sua idade: '))

print(f"Seja bem-vindo {nome} {sobrenome}.")
print(f"Você possui {idade} anos de idade.")
 