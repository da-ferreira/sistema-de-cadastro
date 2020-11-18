
from entrada_funcoes import ler_nome, ler_genero, ler_data_nascimento, ler_estado_civil, idade, linha, mensagem, cor


def arquivo_existe(nome):
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def adicionar_dados(nome_arquivo):
    nome = ler_nome()
    genero = ler_genero()
    nascimento = ler_data_nascimento()
    estCivil = ler_estado_civil()
    anos = idade(nascimento)

    with open(nome_arquivo, 'a') as cadastro:
        cadastro.write(f'{nome};{genero};{nascimento};{estCivil};{anos}\n')
    print(f'{cor["cyan"]}Novo cadastro de {nome} adicionado com sucesso.{cor["l"]}')
    

def mostrar_dados(nome_arquivo):
    print('¬¬¬' * 33)
    if arquivo_existe(nome_arquivo):
        print(f'{"Nome":>7}{"Gênero":>50}{"Nascimento" :>15}{"Estado Civil":>17}{"Idade":>9}')
        print('¬¬¬' * 33)
        with open(nome_arquivo, 'r') as cadastro:
            for dados in cadastro:
                dados = dados.strip().split(';')
                print(f'{dados[0] :<50}{dados[1] :<12}{dados[2] :<15}{dados[3] :<17}{dados[4] :>3}')
    else:
        abrir = open(nome_arquivo, 'a')
        abrir.close()
        print(f'{cor["cyan"]}Arquivo inexistente. Arquivo "{nome_arquivo}" criado com sucesso.{cor["l"]}')
    print('¬¬¬' * 33)
