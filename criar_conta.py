from Cliente import Cliente
import pandas as pd


class criar_conta:
    #Construtor    
    def __init__(self,nome_cliente,cpf,tipo_conta):
        # Intancio o cliente
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta)
        
    def salvar_excel(self,caminho_excel):
        
        dados_cliente = self.cliente.dicionario_cliente()
        
        excel = pd.DataFrame(dados_cliente)
        excel.to_excel(caminho_excel,index=False)
        return excel