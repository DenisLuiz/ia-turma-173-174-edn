#Quero saber se um dia é util ou não

dia = input("Digite o dia da semana: ").lower()

if dia in("sábado", "sabado", "domingo"):
    print("É fim de semana! Uhuuul!")
else:
    print("É dia útil")