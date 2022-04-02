nivel = input("Qual é seu nível de assinatura? ")

if nivel.upper() == "BASIC":
    faturamento = input("Qual foi o faturamento anual do canal? ")
    basic = float(faturamento) * 0.3
    print(f"O bônus a ser pago é de: {basic}")

if nivel.upper() == "SILVER":
    faturamento = input("Qual foi o faturamento anual do canal? ")
    silver = float(faturamento) * 0.2
    print(f"O bônus a ser pago é de: {silver}")

if nivel.upper() == "GOLD":
    faturamento = input("Qual foi o faturamento anual do canal? ")
    gold = float(faturamento) * 0.1
    print(f"O bônus a ser pago é de: {gold}")

if nivel.upper() == "PLATINUM":
    faturamento = input("Qual foi o faturamento anual do canal? ")
    platinum = float(faturamento) * 0.05
    print(f"O bônus a ser pago é de: {platinum}")
