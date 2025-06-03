#Importação de bibliotecas 
from time import sleep

# Criação da interface do systema 
def leiaint(msg):
    while True:
        try:
            numero = int(input(f"{msg}"))
        except(ValueError, TypeError):
            print(f"\33[31mDigite um número\33[m")
        except(KeyboardInterrupt):
            print("\33[mO usuário preferiu não digitar esse número\33[m")
        else:
            return numero
         
def linha(receba = 42):
    tamanho = "-" * receba
    return tamanho

def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu (lista):
    cabecalho("\33[35m MENU PRINCIPAL\33[m")
    contador = 1
    for item in lista:
        sleep(0.30)
        print(f"{contador} - \33[32m{item}\33[m")
        contador += 1
    print(linha())
    opcao = leiaint("\33[36mSua opção: \33[m")
    return opcao
  

