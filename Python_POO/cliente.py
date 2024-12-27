from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, 
                 nome,
                 dataNascimento,
                 cpf, 
                 rg, 
                 nome_mae, 
                 nome_pai, 
                 cep, 
                 endereco, 
                 cidade, 
                 bairro, 
                 estado, 
                 titular, 
                 tipo_conta, 
                 numero_conta, 
                 numero_agencia):

        super().__init__(nome,
                         dataNascimento, 
                         cpf, 
                         rg, 
                         nome_mae, 
                         nome_pai, 
                         cep, 
                         endereco, 
                         cidade, 
                         bairro, 
                         estado)
        
        self.titular             = titular
        self.tipo_conta          = tipo_conta
        self.numero_conta        = numero_conta
        self.agencnumero_agencia = numero_agencia

        '''
        Cliente().__init__(nome, cpf, rg, nome_mae, nome_pai, cep, endereco, cidade, bairro, estado)
        '''