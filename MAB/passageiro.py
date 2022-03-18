from pessoa import Pessoa
from viagem import Viagem

class Passageiro(Pessoa):
    def __init__(self,deficiencia: str, nome: str, cpf: str, idade: int, telefone: int):
        Pessoa.__init__(self,nome,cpf,idade,telefone)
        self.__deficiencia = deficiencia
        #self._cadastroPa = {}
        self._listaPa = []
        self.__acess_Vi = None
        self.__embarque = None
        self.__destino = None
    
        @property
        def deficiencia(self):
            return self.__deficiencia

        @deficiencia.setter
        def deficiencia(self,deficiencia):
            self.__deficiencia=deficiencia
        
        @property
        def acess_Vi(self):
            return self.__acess_Vi
        
        @acess_Vi.setter
        def acess_Vi(self,acess_Vi):
            self.__acess_Vi = acess_Vi

        @property
        def embarque(self):
            return self.__embarque

        @embarque.setter
        def embarque(self, embarque):
            self.__embarque = embarque
        
        @property
        def destino(self):
            return self.__destino
        
        @destino.setter
        def destino(self, destino):
            self.__destino = destino

    def infoPA(self) -> None:
        return f'Nome: {self.__nome}, \nCPF: {self.__cpf}, \nIdade: {self.__idade}, \nTelefone: {self.__telefone}, \nTipo de Deficiência: {self.__deficiencia}'

    def addP(self,nome,cpf,idade,telefone,deficiencia) -> None:
        self._listaPa.append(self)
        return self._listaPa

    def listarP(self) -> None:
        return self._listaPa

    def removerP(self,nome,cpf,idade,telefone,deficiencia) -> None:
        self._listaPa.remove(self)
        print('Passageiro removido com sucessso.')

    def editarP(self,nome_edit,cpf_edit,idade_edit,telefone_edit,deficiencia_edit) -> None:
        self.__nome = nome_edit
        self.__cpf = cpf_edit
        self.__idade = idade_edit
        self.__telefone = telefone_edit
        self.__deficiencia = deficiencia_edit
        print('Cadastro editado com sucesso.')

    def cancelar_viagem(self) -> None:
        self.__acess_Vi.remove(self)
        print('Viagem cancelada com sucesso!')

    def pedir_viagem(self) -> None:

        print("Viagem solicitada com sucesso!")

Viagem().listaVi = Passageiro().acess_Vi