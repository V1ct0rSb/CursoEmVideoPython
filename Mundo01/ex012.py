num = float(input("Qual é o preço do produto? R$ "))
print(
    f"O produto que custava {num}, na promoção com desconto de 5% vai custar R$ {num - ((num * 5) / 100):.2f}")
