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

    def cadastrar_VE(self, modelo, cor, placa, renavam, chassi):
        modelo = input("Digite aqui o modelo do seu automóvel: ")
        cor = input("Agora digite a cor: ")
        placa = input("Digite a placa do seu automóvel: ")
        renavam = input("Agora digite o seu renavam: ")
        chassi = input(
            "E para finalizar seu cadastro, digite o chassi do seu automóvel: ")
        print("O cadastro do seu veículo foi finalizado com sucesso!")

    def addVE_lista(self, modelo, cor, placa, renavam, chassi):
        self.veiculos.append(modelo, cor, placa, renavam, chassi)

    def listarVE(self):
        for veiculo in self.veiculos:
            print(f'Suas informações são:\n-{self._modelo} é o modelo do seu veículo; \n-{self._cor} é a cor do seu veículo; \n-{self._placa} está é a placa do seu veículo; \n-{self._renavam} este é o seu renavam; \n-{self._chassi} e este é o chassi do veículo.')

#    def infoVE(self):#        
#       if self.renavam == renavam:
#            print()
#
# perguntar a prof sobre como puxamos o valor de um item da lista, para listar todo o cadastro da pessoa.

    def removerVE(self, modelo, cor, placa, renavam, chassi):
        self.veiculos.remove([modelo, cor, placa, renavam, chassi])
        print("Veículo removido com sucesso!")
