class Aluno:
	def __init__(self, nome, numero, nota_teste, nota_trabalho, nota_projeto, nota_prova, nota_comportamento):
		self.nome = nome 
		self.numero = numero
		self.nota_teste = nota_teste
		self.nota_trabalho = nota_trabalho
		self.nota_projeto = nota_projeto
		self.nota_prova = nota_prova
		self.nota_comportamento = nota_comportamento
		self.media = (nota_teste + nota_trabalho + nota_projeto + nota_prova + nota_comportamento) / 2
		

def cadastrar_aluno(lista):
	lista.append(Aluno(
	input('Nome do aluno: ').title(),
	int(input('N° do aluno: ')),
	float(input('Nota do teste: ')),
	float(input('Nota de trabalho: ')),
	float(input('Nota de projeto: ')),
	float(input('Nota da prova: ')),
	float(input('Nota de comportamento: '))
	))
	
	print('\n')
	return lista

def banner(msg):
	print('-=' * 25)
	print(f'{msg.upper():^45}')
	print('-=' * 25)
	print('\n')
