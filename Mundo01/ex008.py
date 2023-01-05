num = int(input("Uma distância em metros: "))
print(f"""
A medida de {num:.1f} corresponde a
{num/1000}km
{num/100}hm
{num/10}dam
{num*10}dm
{num*100}cm
{num*1000}mm
""")
