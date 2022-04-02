batimentos = int(input("Por favor, insira o número de batimentos por minuto: "))
idade = int(input("Quantos anos você tem? "))

if idade <= 2 and batimentos in range (120, 140):
    print("Saudável.")

if idade >= 8 and idade <= 17 and batimentos in range (80, 100):
    print("Saudável.")

if idade >= 18 and idade <= 59 and batimentos in range (70, 80):
    print("Saudável.")

if idade >= 60 and batimentos in range (50, 60):
    print("Saudável.")

#abaixo

if idade <= 2 and batimentos < 120:
    print("Abaixo da faixa adequada.")

if idade >= 8 and idade <= 17 and batimentos < 80:
    print("Abaixo da faixa adequada.")

if idade >= 18 and idade <= 59 and batimentos < 70:
    print("Abaixo da faixa adequada.")

if idade >= 60 and batimentos < 50:
    print("Abaixo da faixa adequada.")

#acima

if idade <= 2 and batimentos > 140 :
    print("Acima da faixa adequada.")

if idade >= 8 and idade <= 17 and batimentos > 100:
    print("Acima da faixa adequada.")

if idade >= 18 and idade <= 59 and batimentos > 80:
    print("Acima da faixa adequada.")

if idade >= 60 and batimentos > 60:
    print("Acima da faixa adequada.")