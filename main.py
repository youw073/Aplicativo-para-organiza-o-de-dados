# BIBLIOTECAS
import os


# FUNÇÕES
def buscar_nome(nome):
    with open('nomes.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    encontrado = False
    j = 0
    for linha in linhas:
        if j == 1:
            while '=>' not in linha:
                print(linha)
                break
        if nome.lower() in linha.lower() and '=>' in linha.lower():
            encontrado = True
            print(linha)
            j = 1



# CODIGO PRINCIPAL
a = 1
while True:
    print('-' * 35)
    print('             RESERVAS')
    print('-' * 35)
    comando_1 = int(input("""O que você deseja?
    [1] Adicionar usuário
    [2] Procurar usuário
    [3] Sair do aplicativo
    """))

    if comando_1 == 1:
        nome = str(input('Digite o nome do novo usuário: '))
        with open('nomes.txt', 'a') as arquivo:
            arquivo.write(nome + '=>' + '\n')
        informacoes = str(input('Digite todas as informações do usuário, separe-as por enter. (DIGITE "sair" para sair)\n')).lower()
        if informacoes == 'sair':
            a = 0
        else:
            with open('nomes.txt', 'a') as arquivo:
                arquivo.write(informacoes + '\n')
        while True:
            informacoes = str(input('')).lower()
            if informacoes == 'sair':
                a = 0
                break
            else:
                with open('nomes.txt', 'a') as arquivo:
                    arquivo.write(informacoes + '\n')

    elif comando_1 == 2:
        nome = str(input('Digite o nome do usuário: '))
        buscar_nome(nome)
    elif comando_1 == 3:
        print('Saindo do aplicativo...')
        exit()

    else:
        print('Opção inválida! Tente novamente.')
