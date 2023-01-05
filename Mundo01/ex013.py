num = float(input("Qual é o salário do Funcionário? R$ "))
print(
    f"Um funcionário que ganahava R${num:.2f}, com 15% de aumneto, passa a receber R${num + (num*15/100):.2f}")
