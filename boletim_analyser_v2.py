import fuctions
import os
from rich.progress import track 
from rich.table import Table
from rich.console import Console
from termcolor import colored
from datetime import date

alunos = list()
data = '__log__/data.txt'
user_option = 0

data_atual = date.today()
data_string = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'

bimestres = [1, 2, 3, 4]
turma = int(input('Digite a turma: '))
bimestre = int(input('Qual é o bimestre?: '))

table = Table(title = 'Boletim') 
table.add_column('Nome')
table.add_column('N°')
table.add_column('Média')
console = Console()

while bimestre not in bimestres:
	print(colored('Digite um bimestre válido!\n', 'red'))
	bimestre = int(input('Qual é o bimestre?: '))
	
while True:
	try:
		
		fuctions.banner('CADASTRO')
		fuctions.cadastrar_aluno(alunos)
		user_option = int(input("""
[ 1 ] - Cadastrar um novo aluno.
[ 2 ] - Parar.

(Escolha entre "1" ou "2").

Escolha: """))
		os.system('clear' or 'cls')
		if user_option == 2:
			with open(data, 'a') as save:
				for aluno in alunos:
					save.write(f"""
----------------------------
-= Turma: {turma} =-


Nome: {aluno.nome} - N: {aluno.numero}°

Número: {aluno.numero}
Nota teste: {aluno.nota_teste}
Nota trabalho: {aluno.nota_trabalho}
Nota projeto: {aluno.nota_projeto}
Nota prova: {aluno.nota_prova}
Nota comportamento: {aluno.nota_comportamento}
Média: {aluno.media:.1f}

{bimestre}°  bimestre.
Registro feito em: {data_string}


-----------------------------


""")
			break
			
	except ValueError:
		
		print(colored('Não use "," nas notas! Coloque: "." (não coloque letras em notas).', 'red'))
		
os.system("clear" or "cls")

fuctions.banner('BOLETIM / NOTAS')
for aluno in alunos:
	table.add_row(f'{aluno.nome}', f'{str(aluno.numero)}', f'{str(aluno.media)}')
console.print(table)

print('\nVocê pode acessar os registros e informações de cada aluno no arquivo "data.txt" na pasta "__log__"\n')
input('\nPressione [ enter ] para sair: ')
