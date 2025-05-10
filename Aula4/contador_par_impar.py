pares = 0 
impares = 0

while True:
    entrada = input("Digite um numero intiro(ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        print("Encerrado com sucesso")
        break

    try:
        numero = int(entrada)

        if numero % 2 ==0:
            print(f"O numero {numero} é par. ")
            pares += 1

        else:
            print(f"O numero {numero} é impar." )  
            impares += 1  

    except ValueError:
        print("Erro: Digite apenas numeros inteiros")

print("\nResultado ")
print(f"Numeros pares: {pares}")
print(f"Numeros impares {impares}")     
