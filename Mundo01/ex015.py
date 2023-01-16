dia = int(input("Quantos dias alugados? "))
diaTotal = dia * 60

km = int(input("Quantos Km rodados? "))
kmTotal = km * 0.15

total = diaTotal + kmTotal
print(f"O total a pagar é de R${total:.2f}")
