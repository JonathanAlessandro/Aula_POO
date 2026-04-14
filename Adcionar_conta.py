from Cliente import Cliente
import pandas as pd

class Adcionar_conta:
    
    def __init__(self,nome_cliente,cpf,tipo_conta):
        numero_conta = 0
        agencia = 400
        extrato_bancario = 0
        
        self.cliente = Cliente(nome_cliente,cpf,tipo_conta,numero_conta,agencia,extrato_bancario)
        
    def adicionar(self, excel):
        
        criar = excel
        proxima_linha = len(criar) # Isso faz ele sempre adicionar na última linha disponível
        ultima_linha = excel.iloc[-1]#verifica ultima linha criada
        
        dados_cliente = {
            "nome_cliente": [self.cliente.nome_cliente],
            "cpf": [self.cliente.cpf],
            "tipo_conta": [self.cliente.tipo_conta],
            "numero_conta": [ultima_linha["numero_conta"]]+1,
            "agencia": [ultima_linha["agencia"]]+1,
            "extrato_bancario": [self.cliente.extrato_bancario],
        }
        
        novo_dado = pd.DataFrame(dados_cliente)
        
        return novo_dado
    
        # criar.loc[proxima_linha, "numero_conta"] = self["numero_conta"][0]
        # criar.loc[proxima_linha, "nome_cliente"] = self["nome_cliente"][0]
        # criar.loc[proxima_linha, "tipo_conta"] = self["tipo_conta"][0]
        # criar.loc[proxima_linha, "cpf"] = self["cpf"][0]
        # criar.loc[proxima_linha, "agencia"] = self["agencia"][0]
        # criar.loc[proxima_linha, "extrato_bancario"] = self["extrato_bancario"][0]
        
        