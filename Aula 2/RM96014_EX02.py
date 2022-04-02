segunda = int(input("Quantos votos segunda-feira recebeu? "))
maior = segunda

terca = int(input("Quantos votos terça-feira recebeu? "))
if maior < terca:
    maior = terca

quarta = int(input("Quantos votos quarta-feira recebeu? "))
if maior < quarta:
    maior = quarta

quinta = int(input("Quantos votos quinta-feira recebeu? "))
if maior < quinta:
    maior = quinta

sexta = int(input("Quantos votos sexta-feira recebeu? "))
if maior < sexta:
    maior = sexta

empate = 0
if maior == segunda:
    empate = empate + 1
    
if maior == terca:
    empate = empate + 1

if maior == quarta:
    empate = empate + 1

if maior == quinta:
    empate = empate + 1

if maior == sexta:
    empate = empate + 1

if maior == segunda and empate == 1:
    print(f"O dia escolhido foi segunda-feira, com {maior} votos.")
if maior == terca and empate == 1:
    print(f"O dia escolhido foi terça-feira, com {maior} votos.")
if maior == quarta and empate == 1:
    print(f"O dia escolhido foi quarta-feira, com {maior} votos.")
if maior == quinta and empate == 1:
    print(f"O dia escolhido foi quinta-feira, com {maior} votos.")
if maior == sexta and empate == 1:
    print(f"O dia escolhido foi sexta-feira, com {maior} votos.")

if empate != 1:
    print(f"Houve um empate!")