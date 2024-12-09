
import time
from abc import ABC

#Apresentação - Alice
#Superclasse abstrata(UsuarioIFRO):

#Usuario(IFRO) é uma superclasse pois herda seus atributos para duas subclasses: Aluno, Servidor. (processo nomeado de Herança)
#além disso, ela é uma classe abstrata pois não pode instanciar objetos, ou seja, não existe um "UsuarioIFRO do tipo UsuarioIFRO"
class UsuarioIFRO(ABC):
  def __init__(self,nome,cpf, matricula, senha):
    self.__nome= nome
    self.__cpf=cpf
    self.__matricula = matricula
    self.__senha=senha

  def get_nome(self):
    return self.__nome 

  def get_cpf(self):
    return self.__cpf

  def get_matricula(self):
    return self.__matricula

  def get_senha(self):
    return self.__senha

  def criar_senha (self):
    while True:
      try:
        self.__senha = int(input("Digite sua senha: "))
        if len(str(self.__senha)) != 4:  # Verificação para garantir que a senha tenha 4 dígitos
            raise ValueError("A senha deve ter exatamente 4 dígitos.")
        return self.__senha
      except ValueError as e:
        print(f"Erro: {e}. Tente novamente.")
        except Exception as e:
        print(f"Erro inesperado: {e}. Tente novamente.")
        return self.__senha
  
  def set_senha(self):
    self.__novasenha =("Digite sua nova senha:")
    self.__novasenha = self.__senha
    print("Senha alterada com sucesso")

#Apresentação - Jamily
#Aluno é subclasse de de UsuarioIFRO pois HERDA seus atributos (herança)
class Aluno(UsuarioIFRO):
  def __init__(self, nome, cpf, matricula, senha, turma):
    super().__init__(nome,cpf,senha, matricula)
    self.__turma=turma

  def get_turma(self):
    return self.__turma

#Função cadastrar Aluno:
  def cadastrar_aluno(self):
    print("Cadastro Aluno,dados necessários:\n\n01-Nome\n02-Matricula\n03-Turma\n04-CPF\n05-Senha\n\n")
    time.sleep(2)

    print("*=*=*"*6)
    self.__nome =input("Digite seu nome: ")
    time.sleep(0.5)

#Condições de validação dos dados do Aluno(a):
    while True:
      turma=input("Digite sua Turma:")
      if len(str(turma))<=30:
        self.__turma=turma
        break
      else:
        print("Digite novamente: ")
      continue
    time.sleep(0.5)
    
#Validação de Identidade:    
    while True:
      cpf=input("Digite seu CPF com 11 dígitos: ")
      if len(str(cpf)) == 11:
        self.__cpf=cpf
        break
      else:
        print("Cpf inválido tente novamente com 11 dígitos:")
        continue
    time.sleep(0.5)
    
#Validação de Matrícula:
    while True:    
      matricula=input("Digite sua Matricula com 13 dígitos:")
      self.__matricula=(matricula)
      if len(str(matricula))==13:
        self.__matricula=matricula
        break
      else:
        print("Matricula inválida tente novamente com 13 dígitos:")
        continue
    time.sleep(0.5)
    
#Validação de senha do Aluno:      
    while True:
      senha= input("Digite sua senha com 4 dígitos: ")
      self.__senha=(senha)
      if len(str(self.__senha))== 4:
        self._senha=senha
        break
      else:
        print("Senha inválida tente novamente com 4 dígitos:")
        continue
    time.sleep(0.5)

#Função para printar os dados dos alunos
  def exibirDados_aluno(self):
    time.sleep(1)
    print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\nMatricula: {self.__matricula}\nSenha:{self.__senha}\nTurma:{self.__turma}")

#Função para atualizar a turma do aluno set:
  def set_turma(self):
    while True:
      resposta = input(f"\n{self.__nome},deseja atualizar sua turma?\n\n[A] Sim\n[B] Não\nResposta: ")
      print("*=*="*6)
      if resposta.upper() == "A":
        nova_turma = input("Digite sua nova turma (máximo 30 caracteres):")
        if len(str(nova_turma)) <= 30:
          self.__turma = nova_turma
          time.sleep(1)
          print("\nTurma atualizada com sucesso:)")
          print("*=*="*6)
          return
     
        else:
          print("A turma deve ter no máximo 30 caracteres. Por favor,digite novamente.")
      elif resposta.upper() == "B":
        print(f"Ok, {self.__nome},você optou por não trocar de turma.")
        break
      else:
        print("Resposta inválida. Por favor, escolha [A] para sim ou [B] para não.")
        break



#Apresentação - Ana Andrade
#Servidor é subclasse de UsuarioIFRO pois HERDA seus atributos (herança)
class Servidor (UsuarioIFRO):
  def __init__ (self,nome,cpf,senha,matricula,departamento):
    super().__init__(nome,cpf,senha,matricula)
    self.__departamento=departamento

  def get_departamento(self):
    return self.__departamento

  def cadastrar_servidor(self):
    time.sleep(1)
    print("Cadastro Servidor, dados necessarios:\n\n01-Nome\n02-Matricula\n03 Departamento\n04-CPF\n05-Senha\n\n")
    time.sleep(1)
    self.__nome =input("Digite seu nome:")
    time.sleep(0.5)
    
    while True:
      departamento=input("Digite seu departamento:")
      if len(departamento)<=30:
        self.__departamento=departamento
        break
      else:
        print("Digite novamente:")
      continue
    time.sleep(0.5)
    
#validação de Cpf:
    while True:
      cpf= input("Digite seu CPF com 11 dígitos:")
      self.__cpf=(cpf)
      if len(str(cpf)) == 11:
        self.__cpf=cpf
        break
      else:
        print("Cpf inválido tente novamente com apenas 11 dígitos:")
        continue
    time.sleep(0.5)
    
#validação de matrícula:
    while True:    
      matricula = input("Digite sua Matricula com 7 dígitos: ")
      if len(str(matricula)) == 7:
        self.__matricula=matricula
        break
      else:
        print("Matricula inválida tente novamente com apenas 7 digitos:")
        continue
    time.sleep(0.5)
    
#validação de senha
    while True:
      senha= input("Digite sua senha com 4 dígitos: ")
      self.__senha=(senha)
      if len(str(self.__senha))== 4:
        self._senha=senha
        break 
      else:
        print("Senha inválida tente novamente com 4 dígitos:")
        continue
    time.sleep(0.5)

  def exibirDados_servidor(self):
    time.sleep(1)
    print("*=*"*6)
    print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\nMatricula: {self.__matricula}\nSenha:{self.__senha}\nDepartamento:{self.__departamento}")
    print("*=*"*6)

#Set escolha do usuário para troca de departamento
  def set_departamento(self):
    while True:
      atualiza = input(f"{self.__nome}, deseja atualizar seu departamento?\n\n[A]Sim\n[B]Não\n\nResposta: ")
      if atualiza.upper() == "A":
        novo_departamento= input("Digite seu novo departamento(máximo 30 caracteres):")
        if len(novo_departamento)<= 50:
          self.__departamento=novo_departamento
          print("Departamento atualizado com sucesso.")
          return
        else:
          print("O departamento deve ter no máximo 30 caracteres. Por favor,digite novamente.")
          break
      elif atualiza.upper() == "B":
        print(f"Ok, {self.__nome},você optou por não trocar de departamento")
        break
      else:
        print("Resposta inválida. Por favor, escolha [A] para sim ou [B] para não.")
        break
# O construtor da classe Recepcionista herda o comportamento do construtor de Servidor
class Recepcionista(Servidor):
  def __init__ (self,nome,cpf,senha,matricula,departamento):
    # Aqui usamos super() para chamar o construtor da classe base (Servidor),
    # que inicializa os atributos nome, cpf, senha, matricula e departamento
  super().__init__(nome,cpf,senha,matricula, departamento)
  
  # Método específico de Recepcionista para liberar visitantes
  def liberarVisitante(self):
  # Pergunta ao recepcionista se ele deseja liberar ou negar o acesso a um visitante
    while True:
      liberar = int(input("Deseja liberar visitante? SIM [1] ou NÃO [2]")):
      if liberar == 1:
        print("Acesso liberado!")
        break
      elif liberar == 2:
        print("Acesso negado!")
        break
      else:
        print("Tente novamente")
        continue
  
#Apresentação - Alice
#  A classe Visitante tem uma relação de associação com a Classe Recepcionista.
# No entanto, ela é independente e não acessa as funções da catraca, como senha e matrícula.
  
class Visitante:
  import time
  def __init__(self,nome,cpf, idade,documento):
    self.__nome= nome
    self.__cpf=cpf
    self.__idade= idade
    self.__documento=documento

  def get_nome(self):
    return self.__nome

  def get_cpf(self):
    return self.__cpf

  def get_idade(self):
    return self.__idade

  def get_documento(self):
    return self.__documento
    
  def cadastrar_visitante(self):
    self.__nome=input("Digite seu nome:")
    time.sleep(0.5)
        
    while True:
      cpf= input("Digite seu CPF com 11 dígitos:")
      self.__cpf=(cpf)
      if len(str(cpf)) == 11:
        self.__cpf=cpf
        break
      else:
        print("Cpf inválido tente novamente com apenas 11 dígitos:")
        time.sleep(0.5)
        continue
        
    while True:
      idade= int(input("Digite sua idade:"))
      self.__idade=(idade)
      if idade>=18:
        break
      else:
        entrada=input("Menor de 18 anos precisa estar acompanhado de um responsável legal Você está acompanhado?\n\n[A]Sim\n[B]Não\n\nResposta:")
        if entrada.upper()=="A":
          break
        else:
          print ("Acesso negado, você é menor de 18 anos!")
          time.sleep (1)
          exit()
              
    while True:
      documento = input("É necessário o documento de identificação (RG, IDENTIDADE, CNH, CARTEIRA DE HABILITAÇÃO): ").strip().upper()
      if documento in ["RG", "IDENTIDADE", "CNH", "CARTEIRA DE HABILITAÇÃO"]:
        self.__documento = documento
        print("Acesso liberado,agora você pode entrar na instituição:)")
        break
      else:
        print("Docuemnto inválido. Por favor, escolha um dos documentos listados")
        time.sleep(0.5)
        continue

  def exibirDados_Visitante(self):
    time.sleep(1)
    print("*=*"*6)
    print(f"Nome: {self.__nome}\nCPF:{self.__cpf}\n Idade:{self.__idade}\n Documento:{self.__documento}")
    print("*=*"*6)

#Classe Catraca tem relação de associação com UsuarioIfro e Relatório
#UsuarioIfro(no acesso dos alunos pelos dado

class Catraca:
  def __init__ (self, biometria, cartao, faceID):
    self.__biometria = biometria
    self.__cartao = cartao
    self.faceID = faceID
    
  def get_biometria(self):
    return self.__biometria
    
  def get_cartao(self):
    return self.__cartao
    
  def get_faceID(self):
    self.__faceID
# Colocar a importaân da classe e a relaçaõ
from datetime import date, time
class Relatorio:
  def __init__(self, id, tipo, dataEntrada, dataSaida=None, visitantes=0):
    self.__id= id
    self.__tipo= tipo
    self.__dataEntrada = dataEntrada
    self.__dataSaida = dataSaida
    self.__Visitantes = visitantes
    
  def get_idRelatorio(self):
    return self.__id
    
  def get_tipoRelatorio(self):
    return self.__tipo
    
  def get_dataEntrada(self):
    return self.__dataEntrada
    
  def get_dataSaida(self):
    return self.__dataSaida
    
  def get_quantVisitantes(self):
    return self.__Visitantes

# Função para exibir o Relatório
def exibirRelatorio(self):
  print(f"ID:{self.__id}")
  print(f"Tipo:{self.__tipo}")
  print(f"Tipo:{self.__dataEntrada.strftime('%Y-%m-%d %H:%M:%S')}")
if self.__dataSaida:  # Se a saída foi registrada
   print(f"Saída: {self.__dataSaida.strftime('%Y-%m-%d %H:%M:%S')}")
else:
  print("Saída: Não registrada.")
  print(f"Visitantes: {self.__visitantes}")

 # Função para registrar a saída
def registrar_saida(self, saida):
  self.__saida = saida
  
    
