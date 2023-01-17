
# Elabore um programa para calcular a hipotenusa de um triângulo.

# Dicas:

# Veja o módulo math (math.hypot);

# Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

from math import hypot

cateto_a=float(input('Digite o Cateto Adjacente: '))
cateto_o=float(input('Digite o Cateto Oposto: '))

hipotenusa = hypot(cateto_a,cateto_o)
 
print(f'Hipotenusa: {hipotenusa}')