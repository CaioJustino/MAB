import PySimpleGUI as sg

DIM=(400,200)
THEME='DarkBlue4'
#FONT='Arial'
sg.theme(THEME)

class Pessoa:
	def __init__(self,nome,CPF):
		self.nome=nome
		self.CPF=CPF

	def __str__(self):
		return f'{self.nome} - {self.CPF}'

	def editPessoa(self,novoNome,novoCPF):
		self.nome=novoNome
		self.CPF=novoCPF

	def addPessoa(self,lista):
		lista.append(self)
		return lista

	def delPessoa(self,lista):
		lista.remove(self)
		return lista

def buscarPessoa(CPF,lista):
	for i in lista:
		if i.CPF == CPF:
			return i
	return False

#########################-MAIN-###############################
#Inicializando
NOMES=['Joao','Maria','Gilberto','Lucas','Gabriela','Conceicao','Alana']
CPFS=['123098','567321','135790','098123','091267','765891','916289']
listaPessoas=[]

for i in range(len(NOMES)):
	pessoa_i=Pessoa(NOMES[i],CPFS[i])
	listaPessoas=pessoa_i.addPessoa(listaPessoas)

#exit()

def pagina1():
	esquerda=[[sg.Text('Nome:'),sg.Input(size=12,key='-NOME-')],
				[sg.Text('CPF:'),sg.Input(size=13,key='-CPF-')],
				[sg.Button('Adicionar'),sg.Button('Buscar')]]

	tabela=[[i.nome,i.CPF] for i in listaPessoas]

	direita=[[sg.Table(tabela, ['Nome','CPF'], num_rows=5,key='-TABELA-')]]

	layout = [[sg.Col(esquerda),sg.Col(direita)]]

	return sg.Window('Grupo de Pessoas', layout,size=DIM,
		element_justification='c',finalize=True)

def pagina2():
	layout=[[sg.Text('Nome:'),sg.InputText('',size=12,key='-NOME2-')],
				[sg.Text('CPF:'),sg.InputText('',size=13,key='-CPF2-')],
				[sg.Button('Excluir'),sg.Button('Editar'),sg.Button('Voltar')]]

	return sg.Window('Exluir e Editar', layout,size=DIM,
		element_justification='c',finalize=True)

#Dinamica
janela1=pagina1()
janela2=pagina2()
janela2.hide()

while True:
	window,event,values=sg.read_all_windows()
	print(event,values)
	
	if event == sg.WIN_CLOSED or event is None:
		break

	if event == 'Adicionar':
		if (values['-NOME-']!='' and values['-CPF-']!='' and
			not buscarPessoa(values['-CPF-'],listaPessoas)):
			pessoa_i=Pessoa(values['-NOME-'],values['-CPF-'])
			listaPessoas=pessoa_i.addPessoa(listaPessoas)
			janela1['-TABELA-'].update([[i.nome,i.CPF] for i in listaPessoas])
		else:
			sg.popup('Error')

	if event == 'Buscar':
		pessoaEncontrada = buscarPessoa(values['-CPF-'],listaPessoas)
		if pessoaEncontrada != False:
			janela2['-NOME2-'].update(values['-NOME-'])
			janela2['-CPF2-'].update(values['-CPF-'])
			janela2.un_hide()
		else:
			sg.popup('Error')

	###

	if event == 'Excluir':
		pessoaEncontrada.delPessoa(listaPessoas)
		janela1['-TABELA-'].update([[i.nome,i.CPF] for i in listaPessoas])

	if event == 'Editar':
		if (values['-NOME2-']!='' and values['-CPF2-']!='' and
			not buscarPessoa(values['-CPF2-'],listaPessoas)):
			pessoaEncontrada.editPessoa(values['-NOME2-'],values['-CPF2-'])
			janela1['-TABELA-'].update([[i.nome,i.CPF] for i in listaPessoas])
		else:
			sg.popup('Error')

	if event == 'Voltar':
		janela2.hide()