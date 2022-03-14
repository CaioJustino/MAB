cadastros = list()

class Pessoa ():
    def __init__(self,nome,cpf,idade,telefone):
        self._nome=nome
        self._cpf=cpf
        self._idade=idade
        self._telefone=telefone
        self.cadastros=[]

        @property
        def nome(self):
          return self._nome

        @property
        def cpf(self):
            return self._cpf

        @property
        def idade(self):
          return self._idade

        @property
        def telefone(self):
          return self._telefone

    def cadastraP(self,nome,cpf,idade,telefone):
      self.cadastros.append([nome,cpf,idade, telefone])
      print(f"Passageiro(a){self._nome} foi cadastrado(a) com sucesso.")
      
#Não sei se é necessário essa lista aqui XD
    def listaP(self):
        print(self._nome)
        print(self._cpf)
        print(self._idade)
        print(self._telefone)

    def editaP (self):
        self._nome = str(input('Edite o Nome:'))
        self._idade = int(input('Edite a Idade:'))
        self._telefone = str(input('Edite o Telefone:'))
        print('Pessoa Editada.')

    def editaNomeP (self):
        self._nome = str(input('Edite o Nome:'))
        print('Nome Editado.')

    def editaIdadeP (self):
        self._idade = int(input('Edite a Idade:'))
        print('Idade editada.')
    
    def editaTelefoneP (self):
        self._telefone = int(input('Edite o Telefone:'))
        print('Telefone Editado.')

    def removeP (self):
        del self._nome
        del self._cpf
        del self._idade
        del self._telefone
        print('Pessoa Removida.')
       
    #falta a classe de cancelamneto de viagem.
