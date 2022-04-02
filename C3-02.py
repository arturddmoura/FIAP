quantidade = int(input("Quantas transações foram realizadas no dia? "))
loop = 1
valortotal = 0
valormedio = 0

while loop <= quantidade:
    valor = int(input(f"Qual foi o valor da transação número {loop}? "))
    loop = loop + 1
    valortotal = valortotal + valor

print(f"O valor total gasto foi de {valortotal}. ")

valormedio = valortotal / quantidade

print(f"O valor médio por transação foi de: {valormedio}")
