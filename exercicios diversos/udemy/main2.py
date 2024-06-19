#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

nota1 = float(input("Informe a nota 1"))
nota2 = float(input("Informe a nota 2"))
media = float((nota1+nota2)/2)

if media > 6:
    print("Aprovado")
else:
    print("Reprovado")
