# Importando biblioteca
import os 
os.system("cls") # limpar o terminal 
from time import sleep 
from lib.arquivo import*
from lib.interface import* 
from pathlib import Path

# Verifica se o arquivo e existente, caso não exista ele cria 
arqui = Path(__file__).parent/'Dias trabalhado.txt'
if not arqui.exists():
    criar_arquivo(arqui)

# Laço para ver dias trabalhados 
while True:
    resposta = menu(['Ver dias trabalhados', 'Cadastra novo', 'Apagar','Total de valor dos dias trabalhados', 'Sair'])

    if resposta == 1:
        sleep(0.5)
        print("\33[32mAnalisando dias trabalhados\33[m")
        sleep(1)
        ler_arquivo(arqui)
        continue

    elif resposta == 2:
        while True:

            print('\33[34mNovo cadastro\33[m')
            dia = int(input("Dia: "))
            valor = float(input('Valor R$: '))
            cadastrar(arqui, dia, valor)

            continuar = str(input("\33[34mDeseja continuar com o cadastro: [S/N] \33[m")).strip().upper()
            while continuar not in "SN":
                print("Digito invalido, [S] para sim e [N] para não")
                continuar = str(input("Deseja continuar com o cadastro: [S/N] ")).strip().upper()
            if continuar == "S":
                continue
            elif continuar == "N":
                break
        

    elif resposta == 3:
        while True:
            
            cabecalho('Apagar dados')
            try:
                dia = float(input('Dia que deseja remover: '))
            except ValueError:
                print('\33[31mDigite um número válido.\33[m')
            else:
                remover_dia(arqui, dia)
        
            remover = str(input("Deseja remover mais algum: [S/N] ")).strip().upper()
            while remover not in "SN":
                print("Digito invalido para sim digite [S] e [N] para não")
                remover = str(input("Deseja remover mais algum: [S/N] ")).strip().upper()
            if remover == "S":
                continue
            elif remover == "N":
                break

    

    elif resposta == 4:
        cabecalho('Opção 3')
        print("Somando valor dos dias trabalhados até agora")
        somar_valores(arqui)

    elif resposta == 5:
        cabecalho("Opção 5")
        cabecalho("Saindo do Sistema")
        break



        
       