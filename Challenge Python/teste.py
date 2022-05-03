#senha, ajuda de senha, telefone, nome, email

lista_pontuação = []
lista_nomes = ["000webhost", "123RF", "500px", "8tracks", "Adobe", "Animal Jam", "AnimeGame", "Animoto", 
    "Apollo", "Appen", "Aptoide", "Armor Games", "Army Force Online", "Audi", "Bitly", 
    "Canva", "Chegg", "Dailymotion", "DataCamp", "Descomplica", ]

lista_vazados = ["email, nome, senha", "email, nome, senha, telefone", "email, nome, senha", "email, senha", 
    "email, ajuda de senha, senha", "email, nome, senha", "email, senha", 
    "email, nome, senha", "email, nome, telefone", "email, senha, nome, telefone", 
    "email, nome, senha", "email, senha", "email, nome, senha", "email, nome, telefone", 
    "email, senha", "email, senha, nome", "email, nome, senha", "email, senha", 
    "email, nome, senha", "email, senha, nome"]

lista_ano = ["2015-03-01", "2020-03-01", "2018-06-01", "2017-07-01", "2013-10-01", "2022-10-01", 
    "2020-02-01", "2018-07-01", "2018-07-01", "2020-06-01", "2020-04-01", "2019-01-01", 
    "2016-05-01", "2019-08-01", "2014-05-01", "2019-05-01", "2018-04-01", "2016-10-01", 
    "2018-12-01", "2021-03-01"]

for i in range(0, len(lista_nomes)):
    print(lista_nomes[i] + " || " + lista_vazados[i] + " || " + lista_ano[i])

'''
1 - Animal Jam
2 - Descomplica
3 - Appen
4 - Aptoide
5 - 123RF
6 - AnimeGame
7 - Canva
8 - Armor Games
9 - DataCamp
10/11 - Animoto
10/11 - Apollo
12 - 500px
13 - Chegg
14 - 8tracks
15 - DailyMotion
16 - Army Force Online
17 - 00webhost
18 - Bitly
19 - Adobe  
20 - Audi
'''