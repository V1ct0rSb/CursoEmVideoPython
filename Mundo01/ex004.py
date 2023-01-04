a = input("Digite algo: ")
print(f"""
O tipo primitivo desse valor é {type(a)}
Só tem espaços? {a.isspace()}
É um número? {a.isnumeric()}
É alfabetico? {a.isalpha()}
É alfanúmerico? {a.isalnum()}
Está em maiúsculo? {a.isupper()}
Está em minúsculo? {a.islower()}
Está capitalizado? {a.istitle()}
""")
