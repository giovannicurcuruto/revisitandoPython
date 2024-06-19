#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
num1 = int(input("informe o primeiro número"))
num2 = int(input("informe o primeiro número"))
sinal = input("Informe o sinal para realizar a operação matematica - só será aceito subtração, divisão, adição e multiplicação!")

match sinal:
    case "+":
        print(f'Adição: {num1*num2}')
    case "-":
        print(f'Subtração: {num1*num2}')
    case "/":
        print(f'Divisão: {num1/num2}')
    case "*":
        print(f'Multiplicação: {num1*num2}')
    case _:
        print("Sinal invalido, programa encerrado")
