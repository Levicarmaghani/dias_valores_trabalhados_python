from lib.interface import *

# Criação do arquivo
def criar_arquivo(nome):
    try:
        abri = open(nome, 'wt+')
        abri.close()
    except:
        print('ERRO! na criação do arquivo')
    else:
        print(f"Arquivo criado com sucesso")

# Criação pra ler o arquivo 
def ler_arquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except:
        print("ERRO ao ler arquivo")
    else:
        cabecalho(f"\33[mDias trabalhados\33[m")
        print(f'{'Dias Uteis':<30}{'Valores'}\n')
        for linha in abrir:
            dado = linha.strip().split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}R${float(dado[1]):<.2f}')

        
# Criação para cadastrar novo dia 
def cadastrar (arqui, dia="Desconhecido", valor="0"):
    try:
        cadastro = open(arqui, 'at')
    except:
        print("ERRO! Não conseguimos seu arquivo")
    else:
        try:
            cadastro.write(f"0{dia};{valor:2f}\n")
        except:
            print("Houve um erro na hora de ler o arquivo")
        else:
            print(f"\033[mNovo registro de {dia} adicionado\033[m")
            cadastro.close()

# Criação da função para remover dias trabalhados
def remover_dia(nome_arquivo, dias):
    try:
        with open(nome_arquivo, 'rt') as arquivo:
            linhas = arquivo.readlines()
    except:
        print('ERRO! ao ler o arquivo.')
        return

    nova_lista = []
    encontrado = False

    for linha in linhas:
        dados = linha.strip().split(';')
        try:
            dia = float(dados[0])  # Lê o dia como float
        except ValueError:
            continue  # Pula se a linha estiver mal formatada

        # Compara com aproximação para evitar erro de ponto flutuante
        if round(dia, 2) != round(dias, 2):
            nova_lista.append(linha)
        else:
            encontrado = True

    if not encontrado:
        print(f'\33[31mNenhum dia encontrado: {dias}\33[m')
        return

    try:
        with open(nome_arquivo, 'wt') as arquivo:
            arquivo.writelines(nova_lista)
    except:
        print('ERRO! ao sobrescrever o arquivo.')
    else:
        print(f'\33[32mCadastro com o dia {dias} removido com sucesso.\33[m')

        
    
# Criação da função para somar valores 
def somar_valores(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt') as arquivo:
            linhas = arquivo.readlines()
    except:
        print('ERRO! ao abrir arquivo')
        return
    total = 0.0

    for linha in linhas:
        dados = linha.strip().split(';')
        if len(dados) >= 2:
            try:
                valor = float(dados[1])
                total += valor
            except (ValueError):
                continue
    print(f'\33[34mTotal recebido em todos os dias trabalhados: R$ {total:.2f}\33[m')




 

    



