class Endereco():
    def __init__(self,rua,numero,cep,bairro,cidade,estado):
        self._rua = rua
        self._numero = numero
        self._cep = cep
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
    
    def infoE(self):
        return f'Rua: {self._rua}\nNúmero: {self._numero}\nCEP: {self._cep}\nBairro: {self._bairro}\nCidade: {self._cidade}\nEstado: {self._estado}'

    def editarE(self,rua_edit,numero_edit,cep_edit,bairro_edit,cidade_edit,estado_edit):
        self._rua = rua_edit
        self._numero = numero_edit
        self._cep = cep_edit
        self._bairro = bairro_edit
        self._cidade = cidade_edit
        self._estado = estado_edit

class ValidarCPF():
    def __init__(self):
        self.__acess_cpf = None
        self._validado = False

    def validar_cpf(self):
        self.__acess_cpf = [int(char) for char in self.__acess_cpf if char.isdigit()]

        if len(self.__acess_cpf) != 11:
            self._validado = False
            return
       
        if self.__acess_cpf == self.__acess_cpf[::-1]:
            self._validado = False
            return

        for i in range(9, 11):
            value = sum((self.__acess_cpf[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != self.__acess_cpf[i]:
                self._validado = False
                return
                
        self._validado = True

class Pessoa():
    def __init__(self, nome, cpf, idade, telefone):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._telefone = telefone
        self._enderecos = []
      
        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self,nome):
            self._nome = nome

        @property
        def cpf(self):
            return self._cpf

        @cpf.setter
        def cpf(self,cpf):
            self._cpf = cpf

        @property
        def idade(self):
            return self._idade

        @idade.setter
        def idade(self,idade):
            self._idade = idade

        @property
        def telefone(self):
            return self._telefone

        @telefone.setter
        def telefone(self,telefone):
            self._telefone = telefone

    def addP(self):
        pass

    def listarP(self):
        pass
  
    def editarP(self):
        pass

    def removerP(self):
        pass 

    def cancelar_viagem(self):
        pass

    def addE(self,rua,numero,cep,bairro,cidade,estado):
        self._enderecos.append(Endereco(rua,numero,cep,bairro,cidade,estado))

    def listarE(self):
        return self._enderecos

    def removerE(self,object):
        del object

class Passageiro(Pessoa):
    def __init__(self, nome, cpf, idade, telefone, deficiencia):
        Pessoa.__init__(self,nome,cpf,idade,telefone)
        self.__acess_Vi = None
        self.__acess_embarque = None
        self.__acess_destino = None
        self.__acess_pag = None
        self.__deficiencia = deficiencia
        self._dicPa = {"-NOME-": self._nome, "-CPF-": self._cpf, "-IDADE-": self._idade, "-FONE-": self._telefone, "-DEFIC-": self.__deficiencia}
        self._listaPa = []
    
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
        def acess_embarque(self):
            return self.__acess_embarque

        @acess_embarque.setter
        def acess_embarque(self, acess_embarque):
            self.__acess_embarque = acess_embarque
        
        @property
        def acess_destino(self):
            return self.__acess_destino
        
        @acess_destino.setter
        def acess_destino(self, acess_destino):
            self.__acess_destino = acess_destino

        @property
        def acess_pag(self):
            return self.__acess_pag
        
        @acess_pag.setter
        def acess_pag(self, acess_pag):
            self.__acess_pag = acess_pag

    def infoPa(self): #Para o Usuário
        return f'Nome: {self._nome}\nCPF: {self._cpf}\nIdade: {self._idade}\nTelefone: {self._telefone}\nTipo de Deficiência: {self.__deficiencia}'

    def infoPa2(self): #Para o Motorista
        return f'Nome: {self._nome}\nIdade: {self._idade}\nTelefone: {self._telefone}\nTipo de Deficiência: {self.__deficiencia}'

    def addP(self):
        self._listaPa.append(self._dicPa)

    def listarP(self):
        return self._listaPa

    def editarP(self,nome_edit,cpf_edit,idade_edit,telefone_edit,deficiencia_edit):
        self._nome = nome_edit
        self._cpf = cpf_edit
        self._idade = idade_edit
        self._telefone = telefone_edit
        self.__deficiencia = deficiencia_edit

    def removerP(self):
        self._listaPa.remove(self._dicPa)

    def pedir_viagem(self,acess_embarque,acess_destino):
        pass
        #self.__acess_Vi.append(self.__acess_embarque)
        #self.__acess_Vi.append(self.__acess_destino)

    def escolher_pag(self,acess_pag):
        pass

class Veiculo():
    def __init__(self, modelo, cor, placa, renavam, chassi):
        self._modelo = modelo
        self._cor = cor
        self._placa = placa
        self._renavam = renavam
        self._chassi = chassi
       
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

    def infoVe(self): #Para o Usuário    
        return f'Modelo: {self._modelo}\nCor: {self._cor}\nPlaca: {self._placa}\nRenavam: {self._renavam}\nChassi: {self._chassi}'

    def infoVe2(self): #Para o Passageiro   
        return f'Modelo: {self._modelo}\nCor: {self._cor}\nPlaca: {self._placa}'
    
    def editarVe(self,modelo_edit,cor_edit,placa_edit,renavam_edit,chassi_edit):
        self._modelo = modelo_edit
        self._cor = cor_edit
        self._placa = placa_edit
        self._renavam = renavam_edit
        self._chassi = chassi_edit

class Motorista(Pessoa):
    def __init__(self, nome,cpf,idade,telefone,cnh,):
        Pessoa.__init__(self,nome,cpf,idade,telefone)
        self.__cnh = cnh
        self.__acess_Vi = None
        self._veiculos = []
        self._dicM = {"-NOME-": self._nome, "-CPF-": self._cpf, "-IDADE-": self._idade, "-FONE-": self._telefone, "-CNH-": self.__cnh}
        self._listaM = []
        self._viAceitas = []

        @property
        def cnh(self):
            return self.__cnh

        @cnh.setter
        def cnh(self,cnh):
            self.__cnh = cnh 

        @property
        def acess_Vi(self):
            return self.__acess_Vi
        
        @acess_Vi.setter
        def acess_Vi(self,acess_Vi):
            self.__acess_Vi = acess_Vi
    
    def infoM(self):        
        return f'Nome: {self._nome}\nCPF: {self._cpf}\nIdade: {self._idade}\nTelefone: {self._telefone}\nCNH: {self.__cnh}'
    
    def infoM2(self):        
        return f'Nome: {self._nome}\nIdade: {self._idade}\nTelefone: {self._telefone}'

    def addP(self):
        self._listaM.append(self._dicM)
            
    def listarP(self):
        return self._listaM

    def editarP(self,nome_edit,cpf_edit,idade_edit,telefone_edit,cnh_edit):
        self._nome = nome_edit
        self._cpf = cpf_edit
        self._idade = idade_edit
        self._telefone = telefone_edit
        self.__cnh = cnh_edit

    def removerP(self):
        self._listaM.remove(self._dicM)

    def aceitar_viagem(self):
        pass

    def addVe(self,modelo,cor,placa,renavam,chassi):
        self._veiculos.append(Veiculo(modelo,cor,placa,renavam,chassi))

    def listarVe(self):
        return self._veiculos

    def removerVe(self,object):
        del object

class Viagem():
    def __init__(self,embarque,destino):
        self._embarque = embarque
        self._destino = destino
        self.__forma_pag = None
        self.__passageiro = None
        self.__motorista  = None
        self.__veiculo = None
        self._listaVi = []

        @property
        def embarque(self):
            return self._embarque

        @embarque.setter
        def embarque(self, embarque):
            self._embarque = embarque
        
        @property
        def destino(self):
            return self._destino
        
        @destino.setter
        def destino(self, destino):
            self._destino = destino

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

    def infoVi(self):
        return f'Embarque: {self._embarque}\nDestino: {self._destino}'
    
    def saveVi(self):
        self._listaVi.append(self._embarque)
        self._listaVi.append(self._destino)
        self._listaVi.append(self.__passageiro)
        self._listaVi.append(self.__motorista)
        self._listaVi.append(self.__veiculo)
        self._listaVi.append(self.__forma_pag)

    def cancelar_viagem(self):
        self._listaVi.remove(self._embarque)
        self._listaVi.remove(self._destino)
        self._listaVi.remove(self.__passageiro)
        self._listaVi.remove(self.__motorista)
        self._listaVi.remove(self.__veiculo)
        self._listaVi.remove(self.__forma_pag)
        
class FormaPagamento():
    def __init__(self, modo_pag):
        self._modo_pag = modo_pag

    def infoPag(self):
        return f'Pagamento: {self._modo_pag}'

# Relações de Associação

ValidarCPF().acess_cpf = Pessoa(1,2,3,4)._cpf

Passageiro(1,2,3,4,5).acess_embarque = Viagem(1,2)._embarque
Passageiro(1,2,3,4,5).acess_destino = Viagem(1,2)._destino
Passageiro(1,2,3,4,5).acess_Vi = Viagem(1,2)._listaVi
Passageiro(1,2,3,4,5).acess_pag = FormaPagamento(1)._modo_pag

Motorista(1,2,3,4,5).acess_Vi2 = Viagem(1,2)._listaVi

Viagem(1,2).passageiro = Passageiro(1,2,3,4,5).infoPa2()
Viagem(1,2).motorista = Motorista(1,2,3,4,5).infoM2()
Viagem(1,2).veiculo = Veiculo(1,2,3,4,5).infoVe2()
Viagem(1,2).forma_pag = FormaPagamento(1).infoPag()