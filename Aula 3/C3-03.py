valorinserido = int(input("Insira seu número da sorte: "))

anterior = 1
proximo = 1 

while proximo != valorinserido:
    proximo = proximo + anterior
    anterior = proximo - anterior

if proximo == valorinserido:
    print("Você venceu!")
    
else:
    print("Você perdeu. Tente novamente!")