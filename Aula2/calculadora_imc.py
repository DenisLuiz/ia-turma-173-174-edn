#calculadora de IMC
#PESO DIVIDIDO PELA ALTURA **2

altura = float(input("digite a sua altura em metros:"))
peso = float(input("Digite o seu peso em kg :"))

imc = peso /(altura ** 2)

print(f" sei IMC é {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Acima do peso")
