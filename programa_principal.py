
from entrada_funcoes import mensagem, linha, cor
from cadastro_funcoes import menu
from arquivo_funcoes import adicionar_dados, mostrar_dados
from time import sleep

arquivo = 'pessoas_cadastradas.txt'

while True:
    opcao = menu()
    
    if opcao == 1:
        mostrar_dados(arquivo)
        sleep(2)
    elif opcao == 2:
        linha('Novo cadastro')
        adicionar_dados(arquivo)
        sleep(1.5)
    elif opcao == 3:
        break
   
linha('Volte sempre!', caractere='~=~')
