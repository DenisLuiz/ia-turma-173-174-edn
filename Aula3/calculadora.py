while True:
    try:
        #numeros com interação do usuário
        num1 = float(input("digite o prmeiro numero: "))
        num2 = float (input("digite o segundo numero: "))

        operation = input("digite a operação (+, -, *, /): ")

        if operation == "+":
            resultado = num1 + num2
        elif operation == "-":
            resultado == num1 - num2
        elif operation == "*":
            resultado = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Voce não pode dividir por zero")
            resultado = num1 / num2
        else:
            raise ValueError("Operação invalida! ")
        
        print(f"resultado: {resultado}")
        break

    except ValueError as e:

        if str(e) == "Operação inválida. ":
            print(e)
        else:
            ("Entrada inválida, isso não é um numero, por favor, digite novamente")
        
    except ZeroDivisionError as e:
        print(e)
            