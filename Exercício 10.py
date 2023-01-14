""" 
Faça um programa que peça uma temperatura em Fahrenheit (F) 
e converta esta temperatura para grau Celsius (C), mostrando o resultado da conversão na tela.

Use a fórmula: C = 5 * ((F-32) / 9).

 """

def to_celsius(fahrenheit):
    celsius = 5 * ((fahrenheit-32) / 9)
    return celsius

c = float(input('Informe a temperatura em Fahrenheit: '))
print(f'A temperatura em Celsius é: {to_celsius(c):.2f}º')