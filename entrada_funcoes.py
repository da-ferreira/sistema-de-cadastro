
cor = {
    "l": '\033[m',
    "red": '\033[1;31m',
    "cyan": '\033[0;36m',
    "azul": '\033[1;34m',
    "verde": '\033[1;32m'
}


def linha(mensagem, caractere='-=-', pular_linha=0, dormir=0.0, centralizar=0):
    from time import sleep
    sleep(dormir)

    if pular_linha == 1:
        print('\n' + f'{caractere * 3} {mensagem} {caractere * 3}'.center(centralizar))
    elif pular_linha == 2:
        print('\n' + f'{caractere * 3} {mensagem} {caractere * 3}'.center(centralizar) + '\n')
    else:
        print(f'{caractere * 3} {mensagem} {caractere * 3}'.center(centralizar))


def ler_nome():
    linha('Nome', caractere='~')
    try:
        nome = input('Nome: ').strip().title()
    except KeyboardInterrupt:
        print(f'{cor["red"]}Usuário preferiu não informar o nome.{cor["l"]}')
        return '<desconhecido>'
    else:        
        if nome == '':
            return '<desconhecido>'
        else:
            return nome


def ler_genero():
    generos = {1: 'Masculino', 2: 'Feminino', 3: 'Outros'}
    
    linha('Gênero', caractere='~')

    print('[ 1 ] Masculino\n[ 2 ] Feminino\n[ 3 ] Outros')
    while True:
        try:
            genero = int(input('Opção: '))
        except (TypeError, ValueError):
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe o gênero corretamente.{cor["l"]}')
        else:
            if genero not in range(1, 4):
                print(f'{cor["red"]}ERRO:{cor["cyan"]} Não existe opção de gênero {genero}.{cor["l"]}')
            else:
                return generos[genero]


def ler_dia():
    while True:
        try:
            dia = int(input('Dia: '))
        except (TypeError, ValueError):
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe o dia de seu nascimento corretamente.{cor["l"]}')
        else:
            if dia not in range(1, 32):
                print(f'{cor["red"]}ERRO:{cor["cyan"]} Não existe dia {dia}.{cor["l"]}')
            else:
                if len(str(dia)) == 1:
                    return f'0{str(dia)}'
                else:
                    return str(dia)


def ler_mes():
    while True:
        try:
            mes = int(input('Mês: '))
        except (TypeError, ValueError):
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe o mês de seu nascimento corretamente.{cor["l"]}')
        else:
            if mes not in range(1, 13):
                print(f'{cor["red"]}ERRO:{cor["cyan"]} Não existe mês {mes}.{cor["l"]}')
            else:
                return mes


def ler_ano():
    from datetime import date
    while True:
        try:
            ano = int(input('Ano: '))
        except (ValueError, TypeError):
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe o ano de seu nascimento corretamente.{cor["l"]}')
        else:
            if ano < 1900 or ano > date.today().year:
                print(f'{cor["red"]}ERRO:{cor["cyan"]} informe apenas o ano entre o intervalo de 1900 a 2020.{cor["l"]}')
            else:
                return ano


def idade(data):
    from datetime import date
    
    ano = data.split('/')
    ano = int(ano[2])
    return date.today().year - ano


def ler_data_nascimento():
    mes_abreviacao = {
        1: 'JAN', 2: 'FEV', 3: 'MAR', 4: 'ABR',
        5: 'MAIO', 6: 'JUN', 7: 'JUL', 8: 'AGO',
        9: 'SET', 10: 'OUT', 11: 'NOV', 12: 'DEZ'
    }

    linha('Data de Nascimento', caractere='~')

    ano = ler_ano()
    mes = mes_abreviacao[ler_mes()]
    dia = ler_dia()

    return f'{dia}/{mes}/{ano}'


def ler_estado_civil():
    estCivis = {
        1: 'Solteiro(a)', 2: 'Casado(a)', 3: 'Separado(a)', 4: 'Viúvo(a)', 5: 'Outro'
    }

    linha('Estado Civil', caractere='~')
    print('[ 1 ] Solteiro(a)\n[ 2 ] Casado(a)\n[ 3 ] Separado(a)\n[ 4 ] Viúvo(a)\n[ 5 ] Outro')

    while True:
        try:
            opcao = int(input('Opção: '))
        except (ValueError, TypeError):
            print(f'{cor["red"]}ERRO:{cor["cyan"]} por favor, informe o estado civil corretamente.{cor["l"]}')
        else:
            if opcao not in range(1, 6):
                print(f'{cor["red"]}ERRO:{cor["cyan"]} Não existe opção de estado civil {opcao}.{cor["l"]}')
            else:
                return estCivis[opcao]


def mensagem(texto, caractere='-', cor_linhas='l', cor_texto='l'):
    print(f'{cor[cor_linhas]}{caractere * (len(texto) + 2)}{cor["l"]}')
    print(f' {cor[cor_texto]}{texto}{cor["l"]} ')
    print(f'{cor[cor_linhas]}{caractere * (len(texto) + 2)}{cor["l"]}')
