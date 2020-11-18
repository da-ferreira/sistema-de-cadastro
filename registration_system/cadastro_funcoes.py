
from entrada_funcoes import mensagem, cor


def menu():
    mensagem('SISTEMA DE CADASTRO', cor_linhas='azul', cor_texto='verde', caractere='~')

    print(f'{cor["azul"]}[ 1 ]{cor["cyan"]} Ver pessoas cadastradas')
    print(f'{cor["azul"]}[ 2 ]{cor["cyan"]} Cadastrar uma nova pessoa')
    print(f'{cor["azul"]}[ 3 ]{cor["cyan"]} Sair do sistema{cor["l"]}')

    while True:
        try:
            opcao = int(input(f'{cor["cyan"]}Opção:{cor["l"]} '))
        except (ValueError, TypeError):
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe a opção corretamente.{cor["l"]}')
        else:
            if opcao not in range(1, 4):
                print(f'{cor["red"]}ERRO:{cor["cyan"]} Não existe opção {opcao}.{cor["l"]}')
            else:
                return opcao


def continuar():
    while True:
        try:
            continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        except IndexError:
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe corretamente.{cor["l"]}')
        else:
            break
    while continuar not in 'SN':
        print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe somente S(sim) ou N(não).{cor["l"]}')
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    return continuar
    
