opções_validas = ["senha", "ajuda da senha", "número do telefone", "nomes", "email", "usuário"]
lista_nomes = ["Adobe", "Apollo", "Canva", "PDL", "Hurb"]
lista_ano = [10/2013, 7/2018, 5/2019, 10/2019, 3/2019]
lista_vazados =["email, dica de senha, senha, usuário", "email, telefone, nome", 
"email, nome, senha, usuário", "email, nome, telefone", "email, nome, senha, telefone"]
lista_pontuação = [0, 0, 0, 0, 0]

lista_sorted = []
lista_resultados = []

rodando = True

while rodando == True:
    menu_opção = int(input("O que deseja fazer?\n1) Adicionar ao banco de dados.\n2) Gerar lista organizada por gravidade.\n3) Parar programa.\nSelecione uma opção: "))

    if menu_opção == 1:
        nome = input("Qual é o nome da empresa que sofreu o vazamento? ")
        lista_nomes.append(nome)
        
        mes = int(input("Qual foi o mês do vazamento? (Sem zeros à esquerda, por favor): "))
        ano = int(input("Qual foi o ano do vazamento? (Com quatro dígitos): "))
        lista_ano.append(mes/ano)

        vazados = input("Quais informações foram vazadas? (As divida por vírgulas, por favor): ")
        lista_vazados.append(vazados)

        lista_pontuação.append(0)
    
    if menu_opção == 2:

        for i in range (0, len(lista_nomes)):
            if "senha" in lista_vazados[i]:
                lista_pontuação[i] = lista_pontuação[i] + 1000
            if "ajuda de senha" in lista_vazados[i]:
                lista_pontuação[i] = lista_pontuação[i] + 750
            if "usuário" in lista_vazados[i]:
                lista_pontuação[i] = lista_pontuação[i] + 500
            if "nome" in lista_vazados[i]:
                lista_pontuação[i] = lista_pontuação[i] + 400
            if "telefone" in lista_vazados[i]:
                lista_pontuação[i] = lista_pontuação[i] + 300
            if "email" in lista_vazados[i]:
                lista_pontuação[i] = lista_pontuação[i] + 200

        for i in range (0, len(lista_ano)):
            lista_ano[i] = float(lista_ano[i])
            lista_pontuação[i] = lista_pontuação[i] + lista_ano[i]

        lista_sorted = sorted(lista_pontuação, reverse = True)

        for i in range(0, len(lista_nomes)):
            j = lista_pontuação.index(lista_sorted[i])
            lista_resultados.append(lista_nomes[j])
            lista_pontuação.remove(lista_sorted[i])
            lista_nomes.remove(lista_nomes[j])

        for i in range (0, len(lista_resultados)):
            print (f"{i + 1} - {lista_resultados[i]}")
    
    if menu_opção == 3:
        print("O programa será fechado. ")
        rodando = False