class Passageiro():
  def __init__(self,deficiencia,nome,cpf,idade,telefone):
    Pessoa.__init__(self,nome,cpf,idade,telefone)
    self._deficiencia=deficiencia
    self._passageiro=[]

  @property
  def deficiencia(self):
    return self._deficiencia

  @deficiencia.setter
  def deficiencia(self,deficiencia):
    self._deficiencia=deficiencia

  def infoPA(self):
    print("Nome:",self.nome,"CPF:",self.cpf,"Idade:",self.idade,"Telefone:",self.telefone,"Tipo de deficiência:",self._deficiencia)

  def pedir_viagem(self):
    print("Viagem solicitada com sucesso!")

  def cadastrarP(self,nome,cpf,idade,telefone,deficiencia):
    self._passageiro.append([nome,cpf,idade,telefone,deficiencia])
    print("Passageiro cadastrado com sucesso!")

  def listarP(self):
    print(self._passageiro)

  def removerP(self,nome,cpf,idade,telefone,deficiencia):
    self._passageiro.remove([nome,cpf,idade,telefone,deficiencia])
    print("Passageiro removido com sucessso!")

  def cancelar_viagem(self):
    print("Viagem cancelada com sucesso!")

  def editarP(self):
    self._deficiencia = str(input('Caso queira modificar \n - Edite o tipo de deficiencia: '))
    print('Cadastro editado com sucesso')