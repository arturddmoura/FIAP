nameslist = ["segunda", "terça", "quarta", "quinta", "sexta"]
votos = []

for i in range (0, 5):
    votodia = int(input(f"Quantos votos {nameslist[0 + i]} recebeu? "))
    votos.append(votodia)

votos.index(max(votos))
print(votos)