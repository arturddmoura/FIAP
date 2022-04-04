segunda = int(input("Quantos votos segunda-feira recebeu? "))
terca = int(input("Quantos votos terça-feira recebeu? "))
quarta = int(input("Quantos votos quarta-feira recebeu? "))
quinta = int(input("Quantos votos quinta-feira recebeu? "))
sexta = int(input("Quantos votos sexta-feira recebeu? "))

if segunda > terca:
    if segunda > quarta:
        if segunda > quinta:
            if segunda > sexta:
                print(f"O dia escolhido foi segunda-feira, com {segunda} votos.")

elif terca > segunda:
    if terca > quarta:
        if terca > quinta:
            if terca > sexta:
                print(f"O dia escolhido foi terça-feira, com {terca} votos.")

elif quarta > terca:
    if quarta > segunda:
        if quarta > quinta:
            if quarta > sexta:
                print(f"O dia escolhido foi quarta-feira, com {quarta} votos.")

elif quinta > terca:
    if quinta > quarta:
        if quinta > segunda:
            if quinta > sexta:
                print(f"O dia escolhido foi quinta-feira, com {quinta} votos.")

elif sexta > terca:
    if sexta > quarta:
        if sexta > quinta:
            if sexta > segunda:
                print(f"O dia escolhido foi sexta-feira, com {sexta} votos.")

else:
    print(f"Houve um empate!")