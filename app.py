import os
def mostra_titulo():
      print("""


      𝓝𝓲𝓮𝓾𝔀𝓮𝓷𝓱𝓸𝓯𝓯 𝓜𝓮𝓭𝓲𝓬𝓲𝓷𝓪

            """)
      
def mostra_escolhas():
      print("1. Cadastro dos alunos")
      print("2. Lista dos alunos")
      print("3. Ativar matricula dos estudantes")
      print("4. Sair da aplicação")

def escolher_opcao():
      opcao_escolhida = int(input('Escolha uma opção: '))

      print("Você escolheu a opção: ", opcao_escolhida)

      def finalizar_programa():
            os.system('cls')
            print('Finalizando programa')

      if opcao_escolhida == 1:
            print('cadastro dos alunod')
      elif opcao_escolhida == 2:
            print('lista dos alunos')
      elif opcao_escolhida == 3:
            print('ativar matricula dos estudantes')
      else:
            finalizar_programa()
def main() :
      mostra_titulo()
      mostra_escolhas()
      escolher_opcao()

if __name__ == '__main__':
      main()
      
      