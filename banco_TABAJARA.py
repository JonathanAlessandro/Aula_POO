from Cliente import Cliente
#    arquivo.py    o nome da nossa classe
import pandas as pd
from criar_conta import criar_conta
import os 

caminho_excel = "cliente_banco_Tabajara.xlsx"

print("================================================")
print("                 BANCO TABAJARA")
print("                                 ")
print("                 Escolha uma opção")
print("                 1 - Criar conta")
print("                 2 - Acessar conta")
print("================================================\n")
opcao = int(input("R: "))

if opcao == 1:
    print("Opcao 1 selecionada")
    nome_cliente = str(input("Nome completo: "))
    cpf = int(input("CPF: "))
    tipo_conta  = str(input("Tipo da conta que deseja criar:  "))
    
    
    if os.path.exists(caminho_excel):
        print("Caminho existe")
        df = pd.read_excel(caminho_excel)
    else:
        print("caminho não existe")
        criar_conta(nome_cliente,cpf,tipo_conta)
        criar_conta.salvar_excel(caminho_excel)
    df.to_excel(caminho_excel, index=False)
elif opcao == 2:
    print("Opcao 2 selecionada")
