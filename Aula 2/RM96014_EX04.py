minutos = int(input("Quantos minutos a máquina está marcando? "))
fatorial = 1

while minutos > 1:
    fatorial = fatorial * minutos
    minutos = minutos - 1

print(f"A senha necessária é: LIBERDADE{fatorial}")