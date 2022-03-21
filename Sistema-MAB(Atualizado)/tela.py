from turtle import color
import PySimpleGUI as sg
from classes import Pessoa as p, Endereco as ende, Passageiro as pa, Motorista as m, Veiculo as ve, Viagem as vi, FormaPagamento as pag, ValidarCPF as vcpf

DIM1=(300,100)
DIM2=(600,450)
DIM3=(600,250)
DIM4=(300,200)
DIM5=(200,150)
THEME='DarkBlue15'
sg.theme(THEME)

# Páginas (Layout)

def pagina1():
	layout = [[sg.Text('Bem-vindo(a) ao MAB!', text_color='yellow')],
				[sg.Text('Vocé é:')],
				[sg.Button('Passageiro'),sg.Button('Motorista')]]

	return sg.Window('Início', layout,size=DIM1,element_justification='c',finalize=True)

# Passageiro (Pessoa) - Cadastro

def pagina2():
	pessoa = [[sg.Text('Informações de Pessoa', text_color='yellow')],
				[sg.Text('Nome:'),sg.InputText(size=40,key="-NOME-")],
				[sg.Text('CPF:'),sg.InputText(size=40,key="-CPF-")],
				[sg.Text('Idade:'),sg.InputText(size=40,key="-IDADE-")],
				[sg.Text('Telefone:'),sg.InputText(size=40,key="-FONE-")],
				[sg.Text('Deficiência:'),sg.InputText(size=40,key="-DEFIC-")]]

	endereco = [[sg.Text('Endereço', text_color='yellow')],
				[sg.Text('Rua:'),sg.InputText(size=40,key="-RUA-")],
				[sg.Text('Número:'),sg.InputText(size=40,key="-NUMERO-")],
				[sg.Text('CEP:'),sg.InputText(size=40,key="-CEP-")],
				[sg.Text('Bairro:'),sg.InputText(size=40,key="-BAIRRO-")],
				[sg.Text('Cidade:'),sg.InputText(size=40,key="-CIDADE-")],
				[sg.Text('Estado:'),sg.InputText(size=40,key="-ESTADO-")],
				[sg.Text('\n')],
				[sg.Button('Enviar',key='-ENVIARPA-'),sg.Button('Cancelar',key='-CANCELAR-')]]

	layout = [[pessoa,endereco]] 

	return sg.Window('Cadastro de Passageiro', layout,size=DIM2,finalize=True)

# Motorista (Pessoa) - Cadastro 1

def pagina3():
	pessoa = [[sg.Text('Informações de Pessoa', text_color='yellow')],
				[sg.Text('Nome:'),sg.InputText(size=40,key="-NOME-")],
				[sg.Text('CPF:'),sg.InputText(size=40,key="-CPF-")],
				[sg.Text('Idade:'),sg.InputText(size=40,key="-IDADE-")],
				[sg.Text('Telefone:'),sg.InputText(size=40,key="-FONE-")],
				[sg.Text('CNH:'),sg.InputText(size=40,key="-CNH-")]]

	endereco = [[sg.Text('Endereço', text_color='yellow')],
				[sg.Text('Rua:'),sg.InputText(size=40,key="-RUA-")],
				[sg.Text('Número:'),sg.InputText(size=40,key="-NUMERO-")],
				[sg.Text('CEP:'),sg.InputText(size=40,key="-CEP-")],
				[sg.Text('Bairro:'),sg.InputText(size=40,key="-BAIRRO-")],
				[sg.Text('Cidade:'),sg.InputText(size=40,key="-CIDADE-")],
				[sg.Text('Estado:'),sg.InputText(size=40,key="-ESTADO-")],
				[sg.Text('\n')],
				[sg.Button('Próximo',key='-PROXIMO1-'),sg.Button('Cancelar',key='-CANCELAR-')]]

	layout = [[pessoa,endereco]] 

	return sg.Window('Cadastro de Motorista', layout,size=DIM2,finalize=True)

# Motorista (Pessoa) - Cadastro 2

def pagina4():
	layout = [[sg.Text('Informações de Veículo', text_color='yellow')],
				[sg.Text('Modelo:'),sg.InputText(size=40,key="-MODELO-")],
				[sg.Text('Cor:'),sg.InputText(size=40,key="-COR-")],
				[sg.Text('Placa:'),sg.InputText(size=40,key="-PLACA-")],
				[sg.Text('Renavam:'),sg.InputText(size=40,key="-RENAVAM-")],
				[sg.Text('Chassi:'),sg.InputText(size=40,key="-CHASSI-")],
				[sg.Text('\n')],
				[sg.Button('Enviar',key='-ENVIARM-'),sg.Button('Cancelar',key='-CANCELAR-')]]

	return sg.Window('Cadastro de Motorista', layout,size=DIM3,finalize=True)

# Tela - Passageiro

def pagina5():
	layout = [[sg.Text('Olá, o que você deseja fazer?', text_color='yellow')],
				[sg.Text('\n')],
				[sg.Button('Exibir Dados', key='-DADOSPA-'),sg.Button('Editar Dados', key='-EDITARPA-')],
				[sg.Button('Pedir Viagem'),sg.Button('Excluir Conta', key='-EXCLUIRPA-')],
				[sg.Button('Sair',key='-SAIR-')]]

	return sg.Window('Tela - Passageiro', layout,size=DIM4,finalize=True,element_justification='c')

# Editar Dados - Passageiro

def pagina6():
	pessoa = [[sg.Text('Informações de Pessoa', text_color='yellow')],
				[sg.Text('Nome:'),sg.InputText(size=40,key="-NOME2-")],
				[sg.Text('CPF:'),sg.InputText(size=40,key="-CPF2-")],
				[sg.Text('Idade:'),sg.InputText(size=40,key="-IDADE2-")],
				[sg.Text('Telefone:'),sg.InputText(size=40,key="-FONE2-")],
				[sg.Text('Deficiência:'),sg.InputText(size=40,key="-DEFIC2-")]]

	endereco = [[sg.Text('Endereço', text_color='yellow')],
				[sg.Text('Rua:'),sg.InputText(size=40,key="-RUA2-")],
				[sg.Text('Número:'),sg.InputText(size=40,key="-NUMERO2-")],
				[sg.Text('CEP:'),sg.InputText(size=40,key="-CEP2-")],
				[sg.Text('Bairro:'),sg.InputText(size=40,key="-BAIRRO2-")],
				[sg.Text('Cidade:'),sg.InputText(size=40,key="-CIDADE2-")],
				[sg.Text('Estado:'),sg.InputText(size=40,key="-ESTADO2-")],
				[sg.Text('\n')],
				[sg.Button('Editar',key='-EDITARPA2-'),sg.Button('Voltar',key='-BACKPA-')]]

	layout = [[pessoa,endereco]] 

	return sg.Window('Editando Dados - Passageiro', layout,size=DIM2,finalize=True)

# Tela - Motorista

def pagina7():
	layout = [[sg.Text('Olá, o que você deseja fazer?', text_color='yellow')],
				[sg.Text('\n')],
				[sg.Button('Exibir Dados', key='-DADOSM-'),sg.Button('Editar Dados', key='-EDITARM-')],
				[sg.Button('Aceitar Viagem'),sg.Button('Excluir Conta', key='-EXCLUIRM-'),],
				[sg.Button('Sair',key='-SAIR-')]]

	return sg.Window('Tela - Motorista', layout,size=DIM4,finalize=True,element_justification='c')

# Editar Dados - Motorista 1

def pagina8():
	pessoa = [[sg.Text('Informações de Pessoa', text_color='yellow')],
				[sg.Text('Nome:'),sg.InputText(size=40,key="-NOME2-")],
				[sg.Text('CPF:'),sg.InputText(size=40,key="-CPF2-")],
				[sg.Text('Idade:'),sg.InputText(size=40,key="-IDADE2-")],
				[sg.Text('Telefone:'),sg.InputText(size=40,key="-FONE2-")],
				[sg.Text('CNH:'),sg.InputText(size=40,key="-CNH2-")]]

	endereco = [[sg.Text('Endereço', text_color='yellow')],
				[sg.Text('Rua:'),sg.InputText(size=40,key="-RUA2-")],
				[sg.Text('Número:'),sg.InputText(size=40,key="-NUMERO2-")],
				[sg.Text('CEP:'),sg.InputText(size=40,key="-CEP2-")],
				[sg.Text('Bairro:'),sg.InputText(size=40,key="-BAIRRO2-")],
				[sg.Text('Cidade:'),sg.InputText(size=40,key="-CIDADE2-")],
				[sg.Text('Estado:'),sg.InputText(size=40,key="-ESTADO2-")],
				[sg.Text('\n')],
				[sg.Button('Próximo',key='-PROXIMO2-'),sg.Button('Voltar',key='-BACKM-')]]

	layout = [[pessoa,endereco]] 

	return sg.Window('Editando Dados - Motorista', layout,size=DIM2,finalize=True)

# Editar Dados - Motorista 2

def pagina9():
	layout = [[sg.Text('Informações de Veículo', text_color='yellow')],
				[sg.Text('Modelo:'),sg.InputText(size=40,key="-MODELO2-")],
				[sg.Text('Cor:'),sg.InputText(size=40,key="-COR2-")],
				[sg.Text('Placa:'),sg.InputText(size=40,key="-PLACA2-")],
				[sg.Text('Renavam:'),sg.InputText(size=40,key="-RENAVAM2-")],
				[sg.Text('Chassi:'),sg.InputText(size=40,key="-CHASSI2-")],
				[sg.Text('\n')],
				[sg.Button('Editar',key='-EDITARM2-'),sg.Button('Cancelar',key='-CANCELAR-')]]

	return sg.Window('Editando Dados - Motorista', layout,size=DIM3,finalize=True)

# Pedir Viagem - Passageiro

def pagina10():
	layout = [[sg.Text('Informações da Viagem', text_color='yellow')],
				[sg.Text('Embarque:'),sg.InputText(size=40,key="-EMBARQ-")],
				[sg.Text('Destino:'),sg.InputText(size=40,key="-DESTIN-")],
				[sg.Text('Forma de Pagamento:'),sg.InputText(size=40,key="-PAG-")],
				[sg.Text('\n')],
				[sg.Button('Enviar',key='-ENVIARVI-'),sg.Button('Voltar',key='-BACKPA2-')]]

	return sg.Window('Pedir Viagem', layout,size=DIM4,finalize=True)

def pagina11():
	layout = [[sg.Text('Opções de Viagem', text_color='yellow')],
				[sg.Text('\n')],
				[sg.Button('Exibir Dados',key='-DADOSVI-'),sg.Button('Cancelar',key='-CANCELVIPA-')]]

	return sg.Window('Tela - Viagem', layout,size=DIM5,finalize=True,element_justification='c')

# Janelas

tela_inicio=pagina1()

tela_cdstPa=pagina2()
tela_cdstPa.hide()
tela_Pa=pagina5()
tela_Pa.hide()
tela_EditPa=pagina6()
tela_EditPa.hide()

tela_cdstM1=pagina3()
tela_cdstM1.hide()
tela_cdstM2=pagina4()
tela_cdstM2.hide()
tela_M = pagina7()
tela_M.hide()
tela_EditM = pagina8()
tela_EditM.hide()
tela_EditM2 = pagina9()
tela_EditM2.hide()

tela_PedirVi=pagina10()
tela_PedirVi.hide()
tela_Vi=pagina11()
tela_Vi.hide()


# Dinâmica do Sistema

while True:
	window,event,values=sg.read_all_windows()
	print(event,values)
	
	if event == sg.WIN_CLOSED or event is None or event == '-CANCELAR-' or event == '-SAIR-':
		break
	
	# Dinâmica - Passageiro -----------------------------------------------------------------

	if event == 'Passageiro':
		tela_cdstPa.un_hide()
		tela_inicio.close()

	if event == '-ENVIARPA-': 
		pa1 = pa(values['-NOME-'],values['-CPF-'],values['-IDADE-'],values['-FONE-'],values['-DEFIC-'])
		ende1 = ende(values['-RUA-'],values['-NUMERO-'],values['-CEP-'],values['-BAIRRO-'],values['-CIDADE-'],values['-ESTADO-'])
		if values['-NOME-'] != '' and values['-CPF-'] != '' and values['-DEFIC-'] != '':
			#vcpf().validar_cpf()
			#if vcpf()._validado == True:
			pa1.addP()
			pa1.addE(values['-RUA-'],values['-NUMERO-'],values['-CEP-'],values['-BAIRRO-'],values['-CIDADE-'],values['-ESTADO-'])
			tela_cdstPa.close()
			tela_Pa.un_hide()
			#else:
				#sg.popup('CPF inválido!')
		else:
			sg.popup('Preencha o formulário!')
	
	if event == '-DADOSPA-':
		sg.popup(pa1.infoPa(),ende1.infoE())

	if event == '-EDITARPA-':
		tela_Pa.hide()
		tela_EditPa.un_hide()

	if event == '-EDITARPA2-':
		pa1.editarP(values['-NOME2-'],values['-CPF2-'],values['-IDADE2-'],values['-FONE2-'],values['-DEFIC2-'])
		ende1.editarE(values['-RUA2-'],values['-NUMERO2-'],values['-CEP2-'],values['-BAIRRO2-'],values['-CIDADE2-'],values['-ESTADO2-'])
		if values['-NOME2-'] != '' and values['-CPF2-'] != '' and values['-DEFIC2-'] != '':
			tela_EditPa.hide()
			tela_Pa.un_hide()
		else:
			sg.popup('Preencha o formulário!')

	if event == '-BACKPA-':
		tela_EditPa.hide()
		tela_Pa.un_hide()

	if event == '-EXCLUIRPA-':
		pa1.removerP()
		pa1.removerE(ende1)
		tela_Pa.close()
		sg.popup('Cadastro removido!')
		break

	# Dinâmica - Motorista --------------------------------------------------------------------

	if event == 'Motorista':
		tela_cdstM1.un_hide()
		tela_inicio.close()

	if event == '-PROXIMO1-':
		tela_cdstM2.un_hide()
		tela_cdstM1.hide()
		m1 = m(values['-NOME-'],values['-CPF-'],values['-IDADE-'],values['-FONE-'],values['-CNH-'])
		ende2 = ende(values['-RUA-'],values['-NUMERO-'],values['-CEP-'],values['-BAIRRO-'],values['-CIDADE-'],values['-ESTADO-'])
		if values['-NOME-'] != '' and values['-CPF-'] != '' and values['-CNH-'] != '':
			m1.addP()
			m1.addE(values['-RUA-'],values['-NUMERO-'],values['-CEP-'],values['-BAIRRO-'],values['-CIDADE-'],values['-ESTADO-'])
		else:
			sg.popup('Preencha o formulário!')
			tela_cdstM1.un_hide()
	
	if event == '-ENVIARM-': 
		ve1 = ve(values['-MODELO-'],values['-COR-'],values['-PLACA-'],values['-RENAVAM-'],values['-CHASSI-'])
		if values['-PLACA-'] != '' and values['-RENAVAM-'] != '' and values['-CHASSI-'] != '':
			m1.addVe(values['-MODELO-'],values['-COR-'],values['-PLACA-'],values['-RENAVAM-'],values['-CHASSI-']) 
			tela_cdstM2.hide()
			tela_M.un_hide()
		else:
			sg.popup('Preencha o formulário!')

	if event == '-DADOSM-':
		sg.popup(m1.infoM(),ende2.infoE(),ve1.infoVe())

	if event == '-EDITARM-':
		tela_M.hide()
		tela_EditM.un_hide()

	if event == '-PROXIMO2-':
		m1.editarP(values['-NOME2-'],values['-CPF2-'],values['-IDADE2-'],values['-FONE2-'],values['-CNH2-'])
		ende2.editarE(values['-RUA2-'],values['-NUMERO2-'],values['-CEP2-'],values['-BAIRRO2-'],values['-CIDADE2-'],values['-ESTADO2-'])
		if values['-NOME2-'] != '' and values['-CPF2-'] != '' and values['-CNH2-'] != '':
			tela_EditM.hide()
			tela_EditM2.un_hide()
		else:
			sg.popup('Preencha o formulário!')
	
	if event == '-BACKM-':
		tela_EditM.hide()
		tela_M.un_hide()
	
	if event == '-EDITARM2-':
		ve1.editarVe(values['-MODELO2-'],values['-COR2-'],values['-PLACA2-'],values['-RENAVAM2-'],values['-CHASSI2-'])
		if values['-PLACA2-'] != '' and values['-RENAVAM2-'] != '' and values['-CHASSI2-'] != '':
			tela_EditM2.hide()
			tela_M.un_hide()
		else:
			sg.popup('Preencha o formulário!')

	if event == '-EXCLUIRM-':
		m1.removerP()
		m1.removerE(ende2)
		m1.removerVe(ve1)
		sg.popup('Cadastro removido!')
		break

	# Dinâmica - Passageiro - Viagem ----------------------------------------------------------

	if event == 'Pedir Viagem':
		tela_Pa.hide()
		tela_PedirVi.un_hide()
	
	if event == '-ENVIARVI-':
		#pa1.pedir_viagem(values['-EMBARQ-'],values['-DESTIN-'])
		vi1 = vi(values['-EMBARQ-'],values['-DESTIN-'])
		pag1 = pag(values['-PAG-'])
		if values['-EMBARQ-'] != '' and values['-DESTIN-'] != '' and values['-PAG-'] != '':
			vi1.saveVi()
			pa1.escolher_pag(values['-PAG-'])
			tela_PedirVi.hide()
			tela_Vi.un_hide()
		else:
			sg.popup('Preencha o formulaário!')

	if event == '-BACKPA2-':
		tela_PedirVi.hide()
		tela_Pa.un_hide()

	if event == '-DADOSVI-':
		sg.popup(vi1.infoVi(),pa1.infoPa2(),pag1.infoPag())

	if event == '-CANCELVIPA-':
		vi1 = vi('','')
		del vi1
		tela_Vi.hide()
		tela_Pa.un_hide()