# Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. 
# Ao fim, calcule seu novo salário considerando cenários hipotéticos, com os seguintes aumentos: 10%, 25%,30% e 50%. 
# A mensagem na tela deverá seguir o seguinte padrão:


# "Olá, [nome] [sobrenome]"
# "Seu salário atual é : [salário]"
# "Seu salário com 10% de aumento é: [salário]"
# "Seu salário com 25% de aumento é: [salário]"
# "Seu salário com 30% de aumento é: [salário]"
# "Seu salário com 50% de aumento é: [salário]"


# No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e após a string, enquanto que o último permite colocar a string no formato titlecased (capitaliza string).

nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
salario = float(input('Digite seu salário: '))

print(f'Olá, {nome} {sobrenome}')
print(f"Seu salário atual é : {salario}")
print(f"Seu salário com 25% de aumento é: {salario*1.25:.2f}")
print(f"Seu salário com 10% de aumento é: {salario*1.10:.2f}")
print(f"Seu salário com 30% de aumento é: {salario*1.30:.2f}")
print(f"Seu salário com 50% de aumento é: {salario*1.50:.2f}")