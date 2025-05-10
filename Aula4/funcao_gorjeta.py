def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
    
    """
    Esta função calcula o valor da gorjeta cm base no total da conta e da porcentagem.
    
    Parâmetros:
    
    valor-conta (float): O valor total da conta %_gorjeta (float: Porcentagem da gorjeta)
    
    Retorna:
        float: Ovalor da gorjeta calculada
    
    """

    gorjeta = valor_conta *(porcentagem_gorjeta / 100)

    return round(gorjeta, 2)
total_conta = float(input("Onformações totais da conta: "))
porcentagem = float(input("Informe a porcentagem da gorjeta: "))

valor_gorjeta = calculo_gorjeta(total_conta, porcentagem)

print(f"Para uma conta de {total_conta:.2f}, uma gorjeta de {porcentagem}% tem ou valor de R${valor_gorjeta}")