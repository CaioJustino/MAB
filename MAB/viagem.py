from passageiro import Passageiro
from motorista import Motorista
from motorista import Veiculo

#classe Forma de Pagamento

class Viagem():
    def __init__(self) -> None:
        self.__embarque = None
        self.__destino = None
        self.__forma_pag = None
        self.__passageiro = None
        self.__motorista  = None
        self.__veiculo = None
        self._listaVi = []

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

        @property
        def forma_pag(self):
            return self.__forma_pag

        @forma_pag.setter
        def forma_pag(self, forma_pag):
            self.__forma_pag = forma_pag

        @property
        def passageiro(self):
            return self.__passageiro
        
        @passageiro.setter
        def passageiro(self, passageiro):
            self.__passageiro = passageiro
        
        @property
        def motorista(self):
            return self.__motorista
        
        @motorista.setter
        def motorista(self, motorista):
            self.__motorista = motorista
        
        @property
        def veiculo(self):
            return self.__veiculo
        
        @veiculo.setter
        def veiculo(self, veiculo):
            self.__veiculo = veiculo

    def infoVi(self) -> None:
        print('Informações da Viagem:')
        self._listaVi.append(self)
        for c in self._listaVi:
            print(c)
    
    def cancelar_viagem(self) -> None:
        self._listaVi.remove(self)
        print('Viagem cancelada com sucesso!')

Viagem().embarque = Passageiro().embarque
Viagem().destino = Passageiro().destino
Viagem().forma_pag = FormaPagamento().modo_pag
Viagem().passageiro = Passageiro().listaPa
Viagem().motorista = Motorista().listaM
Viagem().veiculo = Veiculo().veiculo