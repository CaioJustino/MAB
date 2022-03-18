#class Endereco

class Pessoa():
    def __init__(self, nome: str, cpf: str, idade: int, telefone: str) -> None:
      self.__nome = nome
      self.__cpf = cpf
      self.__idade = idade
      self.__telefone = telefone
    
      @property
      def nome(self):
        return self.__nome

      @nome.setter
      def nome(self,nome):
        self.__nome = nome

      @property
      def cpf(self):
        return self.__cpf

      @cpf.setter
      def cpf(self,cpf):
        self.__cpf = cpf

      @property
      def idade(self):
        return self.__idade

      @idade.setter
      def idade(self,idade):
        self.__idade = idade

      @property
      def telefone(self):
        return self.__telefone

      @telefone.setter
      def telefone(self,telefone):
        self.__telefone = telefone

    def addP(self) -> None:
      pass

    def listarP(self) -> None:
      pass
  
    def editarP(self) -> None:
      pass

    def removerP(self) -> None:
      pass

    def cancelar(self) -> None:
      pass