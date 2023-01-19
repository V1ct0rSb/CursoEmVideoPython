import time

nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
time.sleep(1)

print(f"Seu nome em maiúsculo é {nome.upper()}")
print(f"Seu nome em minúsculo é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome tem {nome.find(' ')}")
