# Desenvolva um programa em Python para calcular a média de notas de alunos 
# em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, 
# em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' 
# para iterar sobre os alunos e suas notas. Além disso, implemente uma estrutura 
# condicional para verificar se cada aluno foi aprovado ou reprovado, considerando
#  que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média 
# e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

qnt_alunos = int(input('Digite a quantidade de alunos: '))
alunos = []

for nome in range(qnt_alunos):
    nome = input(f'Digite o nome do aluno {nome + 0}: ')
    nota1 = float(input('Digite a nota do 1º aluno: '))
    nota2 = float(input('Digite a nota do 2º aluno: '))
    nota3 = float(input('Digite a nota do 3º aluno: '))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'

    alunos.append({
        'nome': nome,
        'notas': [nota1, nota2, nota3],
        'media': media,
        'resultado': resultado
        })

media_geral = sum(aluno["media"] for aluno in alunos) / qnt_alunos

print("\nResultados:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Notas: {aluno['notas']}, Média: {aluno['media']:.2f}, resultado: {aluno['resultado']}")
    
print(f"Média Geral da Turma: {media_geral:.2f}")



    
    
