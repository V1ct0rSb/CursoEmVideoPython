import random

lista = []

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

lista.append(nome1)
lista.append(nome2)
lista.append(nome3)
lista.append(nome4)

random.shuffle(lista)

print(f"""A ordem de apresentação será
{lista}
""")


