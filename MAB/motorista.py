from pessoa import Pessoa

class Veiculo():
    def __init__(self, modelo: str, cor: str, placa: str, renavam: str, chassi: str) -> None:
        self._modelo = modelo
        self._cor = cor
        self._placa = placa
        self._renavam = renavam
        self._chassi = chassi
        self.veiculos = []
        # criar lista para colocar os veículos cadastrados em motorista - fazendo a composição entre as classes.
        # colocar a lista criada em motorista para uma associação em viagem também, já que precisa usar a lista na classe de viagem.

        @property
        def modelo(self):
            return self._modelo

        @property
        def cor(self):
            return self._cor

        @property
        def placa(self):
            return self._placa

        @property
        def renavam(self):
            return self._renavam

        @property
        def chassi(self):
            return self._chassi

    def addVe(self, modelo, cor, placa, renavam, chassi):
        self.veiculos.append(self)

    def listarVE(self):
        for veiculo in self.veiculos:
            print(f'Suas informações são:\n-{self._modelo} é o modelo do seu veículo; \n-{self._cor} é a cor do seu veículo; \n-{self._placa} está é a placa do seu veículo; \n-{self._renavam} este é o seu renavam; \n-{self._chassi} e este é o chassi do veículo.')

#    def infoVE(self):#        
#       if self.renavam == renavam:
#            print()
#
# perguntar a prof sobre como puxamos o valor de um item da lista, para listar todo o cadastro da pessoa.

    def removerVE(self, modelo, cor, placa, renavam, chassi):
        self.veiculos.remove(self)
        print("Veículo removido com sucesso!")

class Motorista():
  def __init__(self, nome,cpf,idade,telefone,cnh,veiculo):
    Pessoa.__init__(self,cnh,veiculo,nome,cpf,idade,telefone)
    self._cnh = cnh
    self._listaM = []
    self.__acess_Vi = None

    @property
    def cnh(self):
      return self._cnh

    @cnh.setter
    def cnh(self,cnh):
      self._cnh=cnh 

    @property
    def acess_Vi(self):
        return self.__acess_Vi
    
    @acess_Vi.setter
    def acess_Vi(self,acess_Vi):
        self.__acess_Vi = acess_Vi
    
    def cadastrarM(self):
        self._listaM.append(self)
        for i in self._listaM:
            print(i)
            
    def editarM(self):
        def editarP(self,nome_edit,cpf_edit,idade_edit,telefone_edit,cnh_edit):
            self.__nome = nome_edit
            self.__cpf = cpf_edit
            self.__idade = idade_edit
            self.__telefone = telefone_edit
            self.__cnh = cnh_edit
            print("Cadastro editado com sucesso.")

    def infoM(self):
        self.motorista.append(self)
        for i in self.motorista:
            print(i)
  
    def removerM(self):
        self.motorista.remove(self)
        for i in self.motorista:
            print(i)
  
    def aceitar_viagem(self):
        print('Viagem aceita!')

    def cancelar_viagem():
        self.__acess_Vi.remove(self)
        print('Viagem cancelada!')