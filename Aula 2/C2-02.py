valorbruto = int(input("Qual é o valor bruto do pacote? "))
categoria = input("Qual é a categoria dos assentos? ")
viajantes = int(input("Qual é a quantidade de viajantes? "))
valorliquido = 0

if categoria.upper() == "ECONÔMICA" and viajantes == 2:
    valorliquido = valorbruto - (float(valorbruto) * 0.03)

if categoria.upper() == "ECONÔMICA" and viajantes == 2:
    valorliquido = valorbruto - (float(valorbruto) * 0.05)

if categoria.upper() == "ECONÔMICA" and viajantes >= 4:
    valorliquido = valorbruto - (float(valorbruto) * 0.05)

#executiva

if categoria.upper() == "EXECUTIVA" and viajantes == 2:
    valorliquido = valorbruto - (float(valorbruto) * 0.05)

if categoria.upper() == "EXECUTIVA" and viajantes == 2:
    valorliquido = valorbruto - (float(valorbruto) * 0.07)

if categoria.upper() == "EXECUTIVA" and viajantes >= 4:
    valorliquido = valorbruto - (float(valorbruto) * 0.08)

#primeira classe

if categoria.upper() == "PRIMEIRA CLASSE" and viajantes == 2:
    valorliquido = valorbruto - (float(valorbruto) * 0.10)

if categoria.upper() == "PRIMEIRA CLASSE" and viajantes == 2:
    valorliquido = valorbruto - (float(valorbruto) * 0.15)

if categoria.upper() == "PRIMEIRA CLASSE" and viajantes >= 4:
    valorliquido = valorbruto - (float(valorbruto) * 0.20)

print(f"O valor bruto da viagem é de: R$ {valorbruto}. ")
print(f"O valor do desconto é de: {valorbruto - valorliquido}. ")
print(f"O valor liquido da viagem é de: {valorliquido}. ")
print(f"O valor por viajante é de {valorliquido / viajantes}. ")