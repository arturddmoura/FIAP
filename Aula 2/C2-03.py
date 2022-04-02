voto = 1
playstation = 0
xbox = 0
nintendo = 0

while voto <= 5:
    opcao = input("Que console você escolhe? ")
    voto = voto + 1
    
    if opcao.upper() == "PLAYSTATION":
        playstation = playstation + 1

    if opcao.upper() == "XBOX":
        xbox = xbox + 1

    if opcao.upper() == "NINTENDO":
        nintendo = nintendo + 1

if nintendo > playstation and nintendo > xbox:
    print(f"O vencedor foi o console da Nintendo, com {nintendo} votos.")

if playstation > nintendo and playstation > xbox:
    print(f"O vencedor foi o Playstation, com {playstation} votos.")

if xbox > playstation and xbox > nintendo:
    print(f"O vencedor foi o Xbox, com {xbox} votos.")