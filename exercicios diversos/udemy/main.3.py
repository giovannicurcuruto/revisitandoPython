#Escreva um programa que resolva uma equação de segundo grau.   
import math
print("Equação de Segundo Grau é composta por aX²+bx+c")

A = int(input("Informe o valor de A - obrigatório"))
B = int(input("Informe o valor de B - obrigatório"))
C = int(input("Informe o valor de C - obrigatório"))

if A == 0:
    print("não é uma equação de segundo grau")
else:
    delta = (B**2) - (4*A*C)
    print(f"Delta: {delta}")
    if delta < 0:
        print ("Não possuem raizes reais")
    elif delta == 0:
        result = -B/ (2*A)
        print(f'A equação possui uma raiz real: x ={result}')
    else:
        x1 = (-B + math.sqrt(delta))/ (2 * A)
        x2 = (-B - math.sqrt(delta))/ (2 * A)
        print(f'A raizes distintas: X1 = {x1} e X2 = {x2}')
    



