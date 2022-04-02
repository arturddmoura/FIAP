aluno = 1
alunopar = 2
notamedia = 0
notaparmedia = 0

while aluno < 50 and aluno % 2 != 0:
    nota = int(input(f"VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {aluno}: "))
    aluno = aluno + 2
    notamedia = notamedia + nota

while alunopar <= 50 and alunopar % 2 == 0:
    notapar = int(input(f"VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {alunopar}: "))
    alunopar = alunopar + 2
    notaparmedia = notaparmedia + notapar

notaparmedia = notaparmedia / 25
notamedia = notamedia / 25

print(f"A média de notas dos alunos ímpares foi de {notamedia}")
print(f"A média de notas dos alunos pares foi de {notaparmedia}")

if notamedia > notaparmedia:
    print(f"A metade ímpar obteve a maior média, com uma média de: {notamedia}")

if notamedia < notaparmedia:
    print(f"A metade par obteve a maior média, com uma média de: {notaparmedia}")

if notamedia == notaparmedia:
    print(f"A metade par e ímpar da sala obtiveram a mesma média.")



    
