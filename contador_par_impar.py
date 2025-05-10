#Contar pares e impares

pares = 0 
impares = 0

while True:
    entrada = input("Digite um numero inteiro(ou'fim' para encerrar):")

    if entrada.lower()=='fim':
        print("Encerrado com sucesso")
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"o numero {numero} é par. ")
            pares += 1
        
        else:
            print(f"o numero {numero} é impar. ")
            impares += 1

    except ValueError:
        print("Erro: Digite apenas numero inteiros")


print("\nResultados: ")
print(f"Numeros pares: {pares}")
print(f"numeros Impares: {impares}")
