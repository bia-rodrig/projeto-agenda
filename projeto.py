import re


def cadastrar_contato(agenda):
	contato = {}
	contato['Nome'] = input('Nome: ')
	contato['Telefone'] = input('Telefone: ')
	while not verifica_telefone(contato['Telefone']):        
		contato['Telefone'] = input('Informe um telefone válido: ')

	contato['Email'] = input('Email: ')
	while not verifica_email(contato['Email']):
		contato['Email'] = input('Informe um e-mail válido: ')
	contato['Favorito'] = False
	agenda.append(contato)

def verifica_telefone(telefone):
	if not all(caractere.isdigit() or caractere in ['(', ')', '-', '+', ' '] for caractere in telefone):
		return False
	return True

def verifica_email(email):
	padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

	if re.match(padrao, email):
		return True
	else:
		return False


def listar_contatos(agenda):
	print('Contatos:')
	for i in agenda:
		print('\n')
		print(f'Nome: {i["Nome"]}')
		print(f'Telefone: {i["Telefone"]}')
		print(f'Email: {i["Email"]}')
		print(f'Favorito: {i["Favorito"]}')


def editar_contato(agenda):
	print('Selecione o contato que deseja editar:')
	for i in range (len(agenda)):
		print(f'{i+1}. {agenda[i]["Nome"]}')
	
	opcao = int(input('Escolha um contato:'))

	contato = {}
	contato['Nome'] = input('Nome: ')
	contato['Telefone'] = input('Telefone: ')
	while not verifica_telefone(contato['Telefone']):        
		contato['Telefone'] = input('Informe um telefone válido: ')

	contato['Email'] = input('Email: ')
	while not verifica_email(contato['Email']):
		contato['Email'] = input('Informe um e-mail válido: ')
	
	contato['Favorito'] = False
	
	agenda[opcao-1] = contato

def marcar_desmarcar_favoritos(agenda):
	print('Marcar/Desmarcar Favoritos')
	for i in range (len(agenda)):
		print(f'{i+1}. {agenda[i]["Nome"]} - Favorito: {agenda[i]["Favorito"]}')
	
	opcao = int(input('Escolha um contato:'))

	if agenda[opcao-1]["Favorito"] == True:
		agenda[opcao-1]["Favorito"] = False
	else:
		agenda[opcao-1]["Favorito"] = True

def listar_favoritos(agenda):
	print('Contatos favoritos')
	for i in range (len(agenda)):
		if agenda[i]["Favorito"] == True:
			print('\n')
			print(f'Nome: {agenda[i]["Nome"]}')
			print(f'Telefone: {agenda[i]["Telefone"]}')
			print(f'Email: {agenda[i]["Email"]}')
			print(f'Favorito: {agenda[i]["Favorito"]}')

def remover_contato(agenda):
	print('Remover contato')
	for i in range (len(agenda)):
		print(f'{i+1}. {agenda[i]["Nome"]}')
	opcao = int(input('Selecione o contato que deseja remover: '))

	contato = agenda.pop(opcao-1)
	print('Contato removido: ' + contato["Nome"])

agenda = []

while True:
	print('\nAgenda de contatos')
	print('1 - Cadastrar contato')
	print('2 - Listar contatos')
	print('3 - Editar contato')
	print('4 - Marcar/Desmarcar como favorito')
	print('5 - Listar favoritos')
	print('6 - Remover contato')
	print('7 - Sair')
	opcao = input('Escolha um opção: ')
	if not opcao.isdigit():
		print('Selecione uma opção válida.')
	else:
		opcao = int(opcao)

	if opcao == 1:
		cadastrar_contato(agenda)
	elif opcao == 2:
		listar_contatos(agenda)
	elif opcao == 3:
		editar_contato(agenda)
	elif opcao == 4:
		marcar_desmarcar_favoritos(agenda)
	elif opcao == 5:
		listar_favoritos(agenda)
	elif opcao == 6:
		remover_contato(agenda)
	elif opcao == 7:
		break
	else:
		print('Digite uma opção válida')
