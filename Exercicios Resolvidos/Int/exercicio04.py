# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

#divisao = int(numero1/numero2) #divisao float
divisao = int(numero1//numero2) #divisao int

print(f"A divisaõ dos numeros fornecidos e igual a: {divisao}")
