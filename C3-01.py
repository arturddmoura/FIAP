quantidade = int(input("Quantos alimentos você ingeriu hoje? "))
loop = 1
caloriasdia = 0

while loop <= quantidade:
    calorias = int(input(f"Quantas calorias o alimento {loop} possui? "))
    loop = loop + 1
    caloriasdia = caloriasdia + calorias

print(f"Você ingeriu: {caloriasdia} calorias hoje.")
