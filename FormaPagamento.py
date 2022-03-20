import PySimpleGUI as sg
# A CLASSE PAGAMENTO
class Pagamento():
    def __init__(self, modo_pag):
        self.modo_pag = modo_pag

    def dinheiro(self):
        self.modo_pag = 'Dinheiro'
        return self.modo_pag

    def cartao(self):
        self.modo_pag = 'Cartão'
        return self.modo_pag
    
    def pix(self):
        self.modo_pag = 'PIX'
        return self.modo_pag

# Interface de pagamento

sg.theme('Dark Blue 3')
layout = [
    [sg.Text('Escolha a forma de pagamento:')],
    [sg.Button('Dinheiro', key='moeda'), sg.Button('Cartão', key='card'), sg.Button('Pix', key='pix')]
]

window = sg.Window('Forma de Pagamento', layout, size=(300, 70))

while True:
    event, values = window.read()
    if event == 'moeda':
        sg.Popup(f'A forma de pagamento será em: {Pagamento(None).dinheiro()}!')
        window.close()
    
    if event == 'card':
        sg.Popup(f'A forma de pagamento será em: {Pagamento(None).cartao()}!')
        window.close()
    
    if event == 'pix':
        sg.Popup(f'A forma de pagamento será em: {Pagamento(None).pix()}!')
        window.close()

    if event == sg.WIN_CLOSED:
        break